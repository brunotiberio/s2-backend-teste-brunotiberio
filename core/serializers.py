from rest_framework import serializers
from .models import Document
from datetime import date, time
from users.models import User
from utils.services import user_get_or_created, import_transactions_from_file


class UploadSerializer(serializers.ModelSerializer):

    id = serializers.UUIDField(read_only=True)
    uploadedFile = serializers.FileField()

    class Meta:
        model = Document
        fields = "__all__"

    def create(self, validated_data):

        upload = Document.objects.create(**validated_data)

        with open(upload.uploadedFile.path, "r", encoding="utf-8") as arquivo:

            for linha in arquivo:

                data_nome_loja = linha[62:81].split()
                data_nome_dono = linha[48:62].split()
                data_cpf = f"{linha[19:30]}"
                data_tipo = int(linha[0])
                data_date = date(int(linha[1:5]), int(linha[5:7]), int(linha[7:9]))
                data_valor = int(linha[9:19]) / 100.00
                data_cartao = f"{linha[30:42]}"
                data_hora = time(
                    int(linha[42:44]), int(linha[44:46]), int(linha[46:48])
                )
                data_saldo = 0

                type_transaction = [2, 3, 9]
                if data_tipo in type_transaction:
                    data_saldo -= data_valor
                else:
                    data_saldo += data_valor

                user = user_get_or_created(
                    data_cpf, data_nome_dono, data_cpf, data_nome_loja, data_saldo
                )

                if user == False:
                    data_saldo_actually = 0

                    get_user = User.objects.filter(cpf=data_cpf)

                    transactions = get_user[0]
                    values_transactions = transactions.transactions.values()
                    type_transaction = [2, 3, 9]

                    for balance in values_transactions:
                        value = float(balance["valor"])
                        if balance["tipo"] in type_transaction:
                            data_saldo_actually -= value
                        else:
                            data_saldo_actually += value

                    data_saldo = data_saldo_actually

                    if data_tipo in type_transaction:
                        data_saldo -= data_valor
                    else:
                        data_saldo += data_valor

                    import_transactions = import_transactions_from_file(
                        data_nome_loja,
                        data_nome_dono,
                        data_tipo,
                        data_date,
                        data_valor,
                        data_cartao,
                        data_hora,
                        data_saldo,
                        get_user[0],
                        data_cpf,
                    )
                else:
                    import_transactions = import_transactions_from_file(
                        data_nome_loja,
                        data_nome_dono,
                        data_tipo,
                        data_date,
                        data_valor,
                        data_cartao,
                        data_hora,
                        data_saldo,
                        user,
                        data_cpf,
                    )

        return upload
