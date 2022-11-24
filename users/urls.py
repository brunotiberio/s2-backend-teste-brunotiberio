from django.contrib import admin
from rest_framework.authtoken.views import obtain_auth_token
from .views import CreateUserView
from django.urls import path

urlpatterns = [
    path("login/", obtain_auth_token, name="user-login"),
    path("user/", CreateUserView.as_view(), name="create-user"),
]
