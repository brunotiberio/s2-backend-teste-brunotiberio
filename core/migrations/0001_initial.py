# Generated by Django 4.1.3 on 2022-11-24 14:46

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Document",
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
                ("title", models.CharField(max_length=200)),
                ("uploadedFile", models.FileField(upload_to="Uploaded Files/")),
                ("dateTimeOfUpload", models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
