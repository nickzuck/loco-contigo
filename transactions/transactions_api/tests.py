from django.test import TestCase
from rest_framework.test import APIRequestFactory
from rest_framework import status
from .models import TransactionModel
from rest_framework.test import APITestCase

class TransactionTests(APITestCase):
    body = {
        "id": 20001,
        "type": "test_type",
        "amount": 1000.12,
    }

    mulitple_transactions = [
        {
            "id" : 10,
            "type" : "cars",
            "amount" : 5000,
        },
        {
            "id": 11,
            "type": "shopping",
            "amount": 10000,
            "parent_id" : 10
        }
    ]
    def create_transaction(self, body = None):
        if body is None:
            body = self.body
        return self.client.post("/transactionservice/transaction", body)

    def test_create_transaction(self):
        response = self.create_transaction()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(TransactionModel.objects.get(id=self.body["id"]).type, self.body["type"])
        self.assertEqual(TransactionModel.objects.count(), 1)

    def test_get_transaction(self):
        id = self.body["id"]
        response = self.client.get(f"/transactionservice/transaction/" + str(id))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


        self.create_transaction()
        response = self.client.get(f"/transactionservice/transaction/" + str(id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_transaction_type(self):
        self.create_transaction()
        id = self.body["id"]
        self.assertEqual(TransactionModel.objects.get(id = id).type, self.body["type"] )

    def test_sum(self):
        for txn_body in self.mulitple_transactions:
            self.create_transaction(body = txn_body)

        self.assertEqual(TransactionModel.objects.count(), 2)
        self.assertEqual(self.client.get("/transactionservice/transaction/sum/11").data, {"sum":10000.0})
        self.assertEqual(self.client.get("/transactionservice/transaction/sum/10").data, {"sum":15000.0})