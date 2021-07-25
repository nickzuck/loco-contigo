from django.db import models

class TransactionModel(models.Model):
    id = models.BigIntegerField(primary_key=True) # BigInteger for long int input
    type = models.CharField(max_length=128)
    amount = models.FloatField()
    parents = models.ManyToManyField('self', through="TransactionParentRelationship", blank=True)

class TransactionParentRelationship(models.Model):
    transaction = models.ForeignKey(TransactionModel, related_name="txn", on_delete=models.CASCADE)
    parent = models.ForeignKey(TransactionModel, related_name="parent", on_delete=models.CASCADE)
    derived = models.BooleanField(default = False)