from rest_framework import serializers
from .models import TransactionModel

class TransactionSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField(read_only=True)  # using IntegerField here since it supports integers till 100 digits
    # type = serializers.CharField(required = True, allow_blank=False)
    # parent_id = serializers.IntegerField(required=False)
    #
    # def create(self, data):
    #     return TransactionModel.objects.create(**data)

    class Meta:
        model = TransactionModel
        fields = ["id", "type", "parent_id"]

