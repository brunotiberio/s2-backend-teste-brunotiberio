from .views import TransactionView, TransactionsCpfDetailView
from django.urls import path

urlpatterns = [
    path("transaction/", TransactionView.as_view(), name="create-transaction"),
    path(
        "transaction/<str:cpf>/",
        TransactionsCpfDetailView.as_view(),
        name="detail-transaction",
    ),
]
