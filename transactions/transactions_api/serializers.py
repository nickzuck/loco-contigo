from rest_framework import serializers
from .models import TransactionModel, TransactionParentRelationship

class TransactionSerializer(serializers.ModelSerializer):
    parent_id = serializers.IntegerField(required=False)

    def create(self, validated_data):
        if "parent_id" in validated_data:
            parent_id = validated_data.pop('parent_id')

        instance = TransactionModel(**validated_data)
        instance.save()
        if parent_id is not None:
            parent_obj = TransactionModel.objects.get(id = parent_id)
            TransactionParentRelationship.objects.create(parent = parent_obj, transaction = instance)
        return instance

    class Meta:
        model = TransactionModel
        fields = ["id", "type", "amount", "parent_id"]

class TransactionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionModel
        fields = ["id"]