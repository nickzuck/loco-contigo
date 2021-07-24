from django.db import models

class TransactionModel(models.Model):
    id = models.BigIntegerField(primary_key=True) # BigInteger for long int input
    type = models.CharField(max_length=128)
    parent_id = models.BigIntegerField(blank = True, null=True)
