from users.models import User
from transactions.models import Transaction


def user_get_or_created(cpf_user, data_nome_dono, data_cpf, data_nome_loja, saldo):

    user = User.objects.filter(cpf=cpf_user)

    if len(user) == 0:
        user_created = User.objects.create_user(
            username=data_nome_dono[0].lower(),
            password=data_cpf,
            first_name=data_nome_dono[0],
            last_name=data_nome_dono[1],
            cpf=data_cpf,
            loja=" ".join(data_nome_loja),
            saldo=saldo,
        )

        return user_created

    return False


def import_transactions_from_file(
    data_nome_loja,
    data_nome_dono,
    data_tipo,
    data_date,
    data_valor,
    data_cartao,
    data_hora,
    data_saldo,
    user,
    cpf,
):

    data_transaction = {}

    data_transaction.update(
        {
            "tipo": data_tipo,
            "data": data_date,
            "valor": data_valor,
            "cartao": data_cartao,
            "hora": data_hora,
            "dono_da_loja": " ".join(data_nome_dono),
            "nome_da_loja": " ".join(data_nome_loja),
            "saldo": data_saldo,
            "user": user,
            "cpf": cpf,
        }
    )

    imported_transaction = Transaction.objects.create(**data_transaction)

    return imported_transaction
