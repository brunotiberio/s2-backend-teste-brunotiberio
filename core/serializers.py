from rest_framework import serializers
from .models import Document


class UploadSerializer(serializers.ModelSerializer):

    id = serializers.UUIDField(read_only=True)
    uploadedFile = serializers.FileField()

    class Meta:
        model = Document
        fields = "__all__"

    def create(self, validated_data):
        # aqui vc deve parsear o arquivo do banco de dados e enviar os dados parserados no bd
        return super().create(validated_data)
