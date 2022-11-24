from rest_framework import generics
from .serializers import TransactionSerializer, TransactionsCPFDetailSerializer
from .models import Transaction
from utils.mixins import SerializerByMethodMixin
from django.shortcuts import get_object_or_404
from users.serializers import UserTransactionSerializer

# Create your views here.


class TransactionView(SerializerByMethodMixin, generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_map = {"POST": TransactionSerializer, "GET": UserTransactionSerializer}


class TransactionsCPFDetailView(SerializerByMethodMixin, generics.ListAPIView):
    queryset = Transaction.objects.all()
    serializer_map = {"GET": TransactionsCPFDetailSerializer}

    lookup_url_kwarg = "cpf"

    def get_queryset(self):

        return self.queryset.filter(cpf=self.kwargs["cpf"])
