from django.db import models

class TransactionModel(models.Model):
    """
    Basic model of the transaction which stores amount and type
    """
    id = models.BigIntegerField(primary_key=True) # BigInteger for long int input
    type = models.CharField(max_length=128)
    amount = models.FloatField()
    parents = models.ManyToManyField('self', through="TransactionParentRelationship", blank=True)

class TransactionParentRelationship(models.Model):
    """
    TransactionParentRelationship stores the transaction and it's related parents

    The main goal of the relationship is to perform a disjoint set kind of operation
    on transactions, such that we can easily fetch the sum of the transactions and
    other transactions related to them
    """
    transaction = models.ForeignKey(TransactionModel, related_name="txn", on_delete=models.CASCADE)
    parent = models.ForeignKey(TransactionModel, related_name="parent", on_delete=models.CASCADE)
    derived = models.BooleanField(default = False)