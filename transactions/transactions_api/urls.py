from django.urls import path

from .views import *

urlpatterns = [
    path("transaction", transaction_create),
    path("transaction/<int:txn_id>", transaction_detail),
    path("transaction/types/<str:type>", transaction_type)
]
