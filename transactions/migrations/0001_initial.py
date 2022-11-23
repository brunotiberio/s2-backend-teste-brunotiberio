# Generated by Django 4.1.3 on 2022-11-23 12:16

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Transaction",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("tipo", models.IntegerField()),
                ("data", models.DateField()),
                ("valor", models.DecimalField(decimal_places=2, max_digits=10)),
                ("cpf", models.CharField(max_length=11)),
                ("cartao", models.CharField(max_length=12)),
                ("hora", models.TimeField()),
                ("dono_da_loja", models.CharField(max_length=14)),
                ("nome_da_loja", models.CharField(max_length=19)),
                ("saldo", models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
