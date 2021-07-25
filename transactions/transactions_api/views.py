from .serializers import TransactionSerializer, TransactionTypeSerializer
from .models import TransactionModel
from rest_framework import generics
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser

# class TransactionCreateView(generics.CreateAPIView):
#     serializer_class = TransactionSerializer
#
# class TransactionUpdateView(generics.UpdateAPIView):
#     serializer_class = TransactionSerializer
#     def get_object(self):
#         return TransactionModel.objects.get(id = self.kwargs.get("txn_id"))
#
# class TransactionListView(generics.ListAPIView):
#     serializer_class = TransactionSerializer
#     queryset = TransactionModel.objects.all()

@api_view(['GET', 'PUT'])
def transaction_detail(request, txn_id):
    """
    Views which operate on a single transaction object, specified by id
    """
    try:
        txn = TransactionModel.objects.get(id = txn_id)
    except ObjectDoesNotExist:
        return Response({"msg" : "Object Not Found"}, status = 404)

    if request.method == "GET":
        serializer = TransactionSerializer(txn)
        return Response(serializer.data)

    if request.method == "PUT":
        data = JSONParser().parse(request)
        data["id"] = txn_id
        serializer = TransactionSerializer(txn, data=data)
        if serializer.is_valid() and serializer.validated_data["id"] == txn.id:
            serializer.save()
            return Response(serializer.data, status = 201)
        # if serializer.is_valid():
        #     return Response({"msg" : "Header and Object Id Mismatch"}, status = 400)
        return Response(serializer.errors, status = 400)

@api_view(["GET"])
def transaction_type(request, type):
    """
    Views which operate on transaction type
    """
    transactions = TransactionModel.objects.filter(type = type)
    serializer = TransactionTypeSerializer(transactions, many=True)
    return Response(map(lambda d: d['id'], serializer.data))
