from .models import dropboxToken
import json
import requests

BASE_URL = "https://api.dropboxapi.com/2/"


def get_user_tokens(session_id):
    user_tokens = dropboxToken.objects.first()
    print(user_tokens)
    if user_tokens is not None:
        return user_tokens
    else:
        return None


def update_or_create_user_tokens(session_id, access_token, state):
    tokens = get_user_tokens(session_id)
    if tokens:
        tokens.access_token = access_token
        tokens.save(update_fields=["access_token"])
    else:
        tokens = dropboxToken(user=session_id, access_token=access_token, state=state)
        tokens.save()


def is_dropbox_authenticated(session_id):
    tokens = get_user_tokens(session_id)
    if tokens:
        return True
    return False


def execute_dropbox_api_request(session_id, endpoint, data, post_=False, put_=False):
    tokens = get_user_tokens(session_id)

    if tokens:
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + tokens.access_token,
        }
    else:
        headers = None

    response = requests.post(
        BASE_URL + endpoint, headers=headers, data=json.dumps(data)
    )

    try:
        response.raise_for_status()  # Raise an exception for non-2xx status codes
        return response.json()
    except requests.exceptions.HTTPError as e:
        print("Error:", e)
        print("Response status code:", response.status_code)
        print("Response content:", response.content)
        return {
            "Error": "Issue with request",
            "Response status code:": response.status_code,
            "Response content:": response.content,
        }


def get_shared_link_file(session_id, endpoint, data, post_=False, put_=False):
    tokens = get_user_tokens(session_id)

    if tokens:
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + tokens.access_token,
        }
    else:
        headers = None

    response = requests.post(
        BASE_URL + endpoint, headers=headers, data=json.dumps(data)
    )

    try:
        response.raise_for_status()  # Raise an exception for non-2xx status codes
        return response.json()
    except requests.exceptions.HTTPError as e:
        print("Error:", e)
        print("Response status code:", response.status_code)
        print("Response content:", response.content)
        return {
            "Error": "Issue with request",
            "Response status code:": response.status_code,
            "Response content:": response.content,
        }
