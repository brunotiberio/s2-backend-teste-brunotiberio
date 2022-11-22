from rest_framework import generics
from .serializers import UploadSerializer
from .models import Document
from utils.mixins import SerializerByMethodMixin

# Create your views here.


class UploadView(SerializerByMethodMixin, generics.ListCreateAPIView):
    queryset = Document.objects.all()
    serializer_map = {
        "GET": UploadSerializer,
        "POST": UploadSerializer,
    }
