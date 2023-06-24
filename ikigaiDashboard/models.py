# Create your models here.

from django.db import models


class NFTSales(models.Model):
    time = models.DateTimeField()
    name = models.CharField(max_length=100)
    highest_sale_price = models.DecimalField(max_digits=10, decimal_places=3)
    current_floor = models.DecimalField(max_digits=10, decimal_places=3)
    objects = models.Manager()

    class Meta:
        db_table = 'nftsales'


class EthereumTraders(models.Model):
    date = models.DateTimeField()
    buyers = models.IntegerField()
    sellers = models.IntegerField()
    unique_traders = models.IntegerField()
    objects = models.Manager()

    class Meta:
        db_table = 'ethereum_traders'


class BTCTraders(models.Model):
    date = models.DateTimeField()
    total_buyers = models.IntegerField()
    total_sellers = models.IntegerField()
    total_traders = models.IntegerField()
    objects = models.Manager()

    class Meta:
        db_table = "btc_traders"
