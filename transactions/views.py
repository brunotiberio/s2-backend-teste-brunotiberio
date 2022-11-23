from rest_framework import generics
from .serializers import TransactionSerializer, TransactionsCpfDetailSerializer
from .models import Transaction
from utils.mixins import SerializerByMethodMixin

# Create your views here.


class TransactionView(SerializerByMethodMixin, generics.CreateAPIView):
    queryset = Transaction.objects.all()
    serializer_map = {
        "POST": TransactionSerializer,
    }


class TransactionsCpfDetailView(SerializerByMethodMixin, generics.RetrieveAPIView):
    queryset = Transaction
    serializer_map = {"GET": TransactionsCpfDetailSerializer}

    lookup_url_kwarg = "cpf"
