from ast import List
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    # path("main/", main),
    path("get-auth-url/", AuthURL.as_view()),
    path("redirect/", dropbox_callback),
    path("is-authenticated/", IsAuthenticated.as_view()),
    path("listit/", List_Items.as_view()),
    path("get-song/<int:id>/", getSong.as_view()),
]
