# Generated by Django 4.2.2 on 2023-07-12 20:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ikigaiDashboard', '0021_delete_bitcointransaction_delete_btcusersdata_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='EthereumTraders',
        ),
    ]
