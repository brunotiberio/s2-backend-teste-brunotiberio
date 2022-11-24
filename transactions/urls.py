from .views import TransactionView, TransactionsCPFDetailView
from django.urls import path

urlpatterns = [
    path("transaction/", TransactionView.as_view(), name="create-transaction"),
    path(
        "transaction/<str:cpf>/",
        TransactionsCPFDetailView.as_view(),
        name="detail-transaction",
    ),
]
