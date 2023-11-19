import os
from django.shortcuts import redirect
from rest_framework.response import Response
from rest_framework import status
from .utils import *
from rest_framework.views import APIView
from .serializers import SongSerializer
from .models import Song
from requests import Request, post, session


class AuthURL(APIView):
    def get(self, request, format=None):
        url = (
            Request(
                "GET",
                "https://www.dropbox.com/oauth2/authorize",
                params={
                    "client_id": os.environ.get("cliend_key"),
                    "redirect_uri": os.environ.get("redirect_uri"),
                    "response_type": "code",
                    "scope": "files.metadata.read files.content.read file_requests.read sharing.read",
                },
            )
            .prepare()
            .url
        )

        return Response({"url": url}, status=status.HTTP_200_OK)


def dropbox_callback(request, format=None):
    code = request.GET.get("code")
    error = request.GET.get("error")

    response = post(
        "https://www.dropbox.com/oauth2/token",
        data={
            "grant_type": "authorization_code",
            "client_secret": os.environ.get("client_secret"),
            "code": code,
            "redirect_uri": os.environ.get("redirect_uri"),
            "client_id": os.environ.get("client_key"),
        },
    ).json()

    access_token = response.get("access_token")
    token_type = response.get("token_type")
    state = response.get("state")
    error = response.get("error")

    if not request.session.exists(request.session.session_key):
        request.session.create()

    update_or_create_user_tokens(request.session.session_key, access_token, state)

    return redirect("http://localhost:5173/playlist/")


class IsAuthenticated(APIView):
    def get(self, request, format=None):
        is_authenticated = is_dropbox_authenticated(self.request.session.session_key)
        return Response({"status": is_authenticated}, status=status.HTTP_200_OK)


class List_Items(APIView):
    def get(self, request, format=None):
        session_id = self.request.session.session_key
        tokens = get_user_tokens(session_id=session_id)
        if tokens:
            endpoint = "files/list_folder"
            data = {
                "include_deleted": False,
                "include_has_explicit_shared_members": False,
                "include_media_info": False,
                "include_mounted_folders": True,
                "include_non_downloadable_files": True,
                "path": "/music",
                "recursive": False,
            }
            response = execute_dropbox_api_request(session_id, endpoint, data)
            if "error" in response or "entries" not in response:
                return Response({}, status=status.HTTP_204_NO_CONTENT)
            entries = response.get("entries")
            if entries:
                for entrie in entries:
                    file_id = entrie.get("id")
                    size = entrie.get("size")
                    download = entrie.get("is_downloadable")
                    name = entrie.get("name")
                    if Song.objects.count() < 10:
                        Song.objects.create(
                            file_id=file_id,
                            size=str(size),
                            is_downloadble=download,
                            name=name,
                        )
                queryset = Song.objects.all()
                serializer = SongSerializer(queryset, many=True)
                response = {"message": "Successfully Done !", "data": serializer.data}
            return Response(response, status=status.HTTP_200_OK)
        return Response({"message": "tokens not found"}, status=status.HTTP_200_OK)


class getSong(APIView):
    def get(self, request, id=id):
        song = Song.objects.get(id=id)
        session_id = self.request.session.session_key
        tokens = get_user_tokens(session_id=session_id)
        if tokens:
            endpoint = "files/get_temporary_link"
            data = {"path": f"/music/{song.name}"}
            response = execute_dropbox_api_request(session_id, endpoint, data).get(
                "link"
            )
            return Response(
                {
                    "link": response,
                },
                status=status.HTTP_200_OK,
            )
        return Response({"message", "sign in first"}, status=status.HTTP_204_NO_CONTENT)
