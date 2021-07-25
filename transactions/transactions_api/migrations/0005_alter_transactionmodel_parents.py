# Generated by Django 3.2.5 on 2021-07-25 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions_api', '0004_auto_20210725_0813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactionmodel',
            name='parents',
            field=models.ManyToManyField(blank=True, related_name='_transactions_api_transactionmodel_parents_+', through='transactions_api.TransactionParentRelationship', to='transactions_api.TransactionModel'),
        ),
    ]
