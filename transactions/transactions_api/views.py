from .serializers import TransactionSerializer, TransactionTypeSerializer
from .models import TransactionModel, TransactionParentRelationship
from rest_framework import generics
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status

@api_view(['POST'])
def transaction_create(request):
    # parent_id = request.data.pop('parent_id', None)
    # parents = [parent_id]
    # if parent_id is not None:
    #     # Fetch all the grandparents of the parent
    #     grandparents = TransactionParentRelationship.objects.filter(transaction= parent_id)
    serializer = TransactionSerializer(data = request.data)
    if serializer.is_valid():
        # serializer.data["parents"] = parents
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT'])
def transaction_detail(request, txn_id):
    """
    Views which operate on a single transaction object, specified by id
    """
    try:
        txn = TransactionModel.objects.get(id = txn_id)
    except ObjectDoesNotExist:
        return Response({"msg" : "Object Not Found"}, status = status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = TransactionSerializer(txn)
        return Response(serializer.data)

    if request.method == "PUT":
        data = JSONParser().parse(request)
        data["id"] = txn_id
        serializer = TransactionSerializer(txn, data=data)
        if serializer.is_valid() and serializer.validated_data["id"] == txn.id:
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        # if serializer.is_valid():
        #     return Response({"msg" : "Header and Object Id Mismatch"}, status = 400)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def transaction_type(request, type):
    """
    Views which operate on transaction type
    """
    transactions = TransactionModel.objects.filter(type = type)
    serializer = TransactionTypeSerializer(transactions, many=True)
    return Response(map(lambda d: d['id'], serializer.data))

@api_view(["GET"])
def transaction_sum(request, txn_id):
    """
    Views for returning the sum by transaction id
    """
    pass