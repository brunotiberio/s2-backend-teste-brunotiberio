from django.db import models
import uuid

# Create your models here.


class Document(models.Model):

    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    title = models.CharField(max_length=200)
    uploadedFile = models.FileField(upload_to="Uploaded Files/")
    dateTimeOfUpload = models.DateTimeField(auto_now=True)

    REQUIRED_FIELDS = ["title"]
