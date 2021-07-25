from django.urls import path

from .views import *

urlpatterns = [
    path("transaction", transaction_create),  # Create transaction
    path("transaction/<int:txn_id>", transaction_detail), # Details of a single transaction
    path("transaction/types/<str:type>", transaction_type),  # List of all the transactions for a type
    path("transaction/sum/<int:txn_id>", transaction_sum) # Heirarchical sum of the transaction
]
