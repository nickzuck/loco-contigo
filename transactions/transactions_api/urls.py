from django.urls import path

from .views import *

urlpatterns = [
    path("transaction", TransactionCreateView.as_view(), name = "create"),
    path("transaction/list", TransactionListView.as_view(), name = "list"),
    path("transaction/update/<int:txn_id>", TransactionUpdateView.as_view(), name = "update")
]
