from .serializers import TransactionSerializer
from .models import TransactionModel
from rest_framework import generics

class TransactionCreateView(generics.CreateAPIView):
    serializer_class = TransactionSerializer

class TransactionUpdateView(generics.UpdateAPIView):
    serializer_class = TransactionSerializer
    def get_object(self):
        return TransactionModel.objects.get(id = self.kwargs.get("txn_id"))


class TransactionListView(generics.ListAPIView):
    serializer_class = TransactionSerializer
    queryset = TransactionModel.objects.all()