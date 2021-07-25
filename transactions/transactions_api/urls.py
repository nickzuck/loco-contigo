from django.urls import path

from .views import *

urlpatterns = [
    # path("transaction", TransactionCreateView.as_view(), name = "create"),
    # path("transaction/list", TransactionListView.as_view(), name = "list"),
    # path("transaction/<int:txn_id>", TransactionUpdateView.as_view(), name = "update"),
    path("transaction/<int:txn_id>", transaction_detail, name = "transaction object op"),
    path("transaction/types/<str:type>", transaction_type, name = "transaction type op")
]
