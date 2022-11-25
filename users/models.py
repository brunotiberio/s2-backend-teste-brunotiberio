from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

# Create your models here.


class User(AbstractUser):

    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=256)
    first_name = models.CharField(max_length=90)
    last_name = models.CharField(max_length=120)
    cpf = models.CharField(max_length=11)
    loja = models.CharField(max_length=256, default='administrador')
    saldo = models.FloatField(default=0.00)

    REQUIRED_FIELDS = ["first_name", "last_name", "password", "cpf"]
