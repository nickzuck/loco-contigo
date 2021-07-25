from .serializers import TransactionSerializer, TransactionTypeSerializer
from .models import TransactionModel, TransactionParentRelationship
from rest_framework import generics
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.db.models import Sum, Count
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status

@api_view(['POST'])
def transaction_create(request):
    """
    View to create a single transaction object
    """
    serializer = TransactionSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT'])
def transaction_detail(request, txn_id):
    """
    Views to get and update a single transaction object
    """
    try:
        txn = TransactionModel.objects.get(id = txn_id)
    except ObjectDoesNotExist:
        return Response({"msg" : "Object Not Found"}, status = status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = TransactionSerializer(txn)
        # serializer.parent_id = txn.parents()
        return Response(serializer.data)

    if request.method == "PUT":
        return Response({"msg" : "NotImplemented"}, status = status.HTTP_501_NOT_IMPLEMENTED)
        # data = JSONParser().parse(request)
        # data["id"] = txn_id
        # serializer = TransactionSerializer(txn, data=data)
        # if serializer.is_valid() and serializer.validated_data["id"] == txn.id:
        #     serializer.save()
        #     return Response(serializer.data, status = status.HTTP_201_CREATED)
        # return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

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
    sum = TransactionModel.objects.filter(Q(parents__id = txn_id) | Q(id=txn_id)).annotate(Count("id")).aggregate(Sum("amount"))
    return Response({"sum" : sum['amount__sum']})