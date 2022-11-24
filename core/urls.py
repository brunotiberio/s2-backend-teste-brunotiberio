from .views import UploadView
from django.urls import path

urlpatterns = [
    path("import/", UploadView.as_view(), name="import-file"),
]