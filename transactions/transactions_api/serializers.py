from rest_framework import serializers
from .models import TransactionModel, TransactionParentRelationship

class TransactionSerializer(serializers.ModelSerializer):
    """
    Serializer to perform CRUD operation on particular transaction object
    """
    parent_id = serializers.IntegerField(required=False)

    def create(self, validated_data):
        """
        Overriding the function to create transaction,
        since we also want to add it's parents and derived parents
        """
        parent_id = None # since there can be no parent
        if "parent_id" in validated_data:
            parent_id = validated_data.pop('parent_id')

        # TODO: [Improvement] Perform the below operation in a atomic transaction, so that we can rollback in case of any failure

        # Create Transaction independent object
        instance = TransactionModel(**validated_data)
        instance.save()

        # Associate the parents and derived parents to the transaction object
        if parent_id is not None:
            parent_obj = TransactionModel.objects.get(id = parent_id)
            TransactionParentRelationship.objects.create(parent = parent_obj, transaction = instance)
            # TODO: [Improvement] Use bulk insert instead of one by one insert OR use atomic transaction
            for grandparent in parent_obj.parents.all():
                TransactionParentRelationship.objects.create(parent = grandparent, transaction = instance, derived = True)
        return instance

    class Meta:
        model = TransactionModel
        fields = ["id", "type", "amount", "parent_id"]

class TransactionTypeSerializer(serializers.ModelSerializer):
    """
    Serializer to return the result of type query independently
    """
    class Meta:
        model = TransactionModel
        fields = ["id"]