from django.shortcuts import render
from rest_framework import generics
from .models import User
from .serializers import UserSerializer, UserTransactionSerializer
from utils.mixins import SerializerByMethodMixin

# Create your views here.


class CreateUserView(SerializerByMethodMixin, generics.ListCreateAPIView):

    queryset = User.objects.all()
    serializer_map = {
        "POST": UserSerializer,
        "GET": UserSerializer,
    }


