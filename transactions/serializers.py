from rest_framework import serializers
from .models import Transaction
from users.models import User


class TransactionSerializer(serializers.ModelSerializer):

    id = serializers.UUIDField(read_only=True)
    user = User()

    class Meta:
        model = Transaction
        fields = "__all__"


class TransactionsCPFDetailSerializer(serializers.ModelSerializer):

    id = serializers.UUIDField(read_only=True)
    # user = UserDetailTransactionSerializer()

    class Meta:
        model = Transaction
        fields = [
            "id",
            "cpf",
            "dono_da_loja",
            "nome_da_loja",
            "tipo",
            "valor",
            "cartao",
            "data",
            "hora",
            "saldo",
            "user",
        ]
        read_only_fields = [
            "id",
            "cpf",
            "dono_da_loja",
            "nome_da_loja",
            "tipo",
            "valor",
            "cartao",
            "data",
            "hora",
            "saldo",
            "user",
        ]
