from rest_framework import serializers
from .models import User
from transactions.serializers import TransactionsCPFDetailSerializer
from transactions.models import Transaction


class LoginSerializer(serializers.ModelSerializer):

    username = serializers.CharField()
    password = serializers.CharField()


class UserSerializer(serializers.ModelSerializer):

    id = serializers.UUIDField(read_only=True)
    password = serializers.CharField(max_length=256, write_only=True)
    transactions = TransactionsCPFDetailSerializer

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "cpf",
            "loja",
            "transactions",
            "password",
            'saldo',
        ]

        read_only_fields = ["id", "is_superuser", "transactions"]


class UserTransactionSerializer(serializers.ModelSerializer):

    id = serializers.UUIDField(read_only=True)

    class Meta:
        model = Transaction
        fields = [
            "id",
            "tipo",
            "data",
            "hora",
            "cartao",
            "user",
            "valor",
            "saldo",
        ]

        ready_only_fields = ["saldo"]
