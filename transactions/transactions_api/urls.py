from django.urls import path

from .views import *

urlpatterns = [
    path("transaction/<int:txn_id>", transaction_detail, name = "transaction object op"),
    path("transaction/types/<str:type>", transaction_type, name = "transaction type op")
]
