from django.db import models
import uuid

# Create your models here.


class Transaction(models.Model):

    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    tipo = models.IntegerField()
    data = models.DateField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    cpf = models.CharField(max_length=11)
    cartao = models.CharField(max_length=12)
    hora = models.TimeField(auto_now=False, auto_now_add=False)
    dono_da_loja = models.CharField(max_length=14)
    nome_da_loja = models.CharField(max_length=19)
    saldo = models.DecimalField(max_digits=10, decimal_places=2)

    REQUIRED_FIELDS = [
        "tipo",
        "data",
        "valor",
        "cpf",
        "cartao",
        "hora",
        "dono_da_loja",
        "nome_da_loja",
    ]
