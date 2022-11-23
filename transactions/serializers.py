from rest_framework import serializers
from .models import Transaction


class TransactionSerializer(serializers.ModelSerializer):

    id = serializers.UUIDField(read_only=True)

    class Meta:
        model = Transaction
        fields = "__all__"


class TransactionsCpfDetailSerializer(serializers.ModelSerializer):

    id = serializers.UUIDField(read_only=True)

    class Meta:
        model = Transaction
        fields = "__all__"
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
        ]
