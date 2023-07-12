# Create your models here.

from django.db import models


class EthereumTraders(models.Model):
    date = models.DateTimeField()
    buyers = models.IntegerField()
    sellers = models.IntegerField()
    traders = models.IntegerField()
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


class TradesByPlatform(models.Model):
    time = models.DateTimeField()
    project = models.CharField(max_length=100)
    trades = models.IntegerField()
    objects = models.Manager()

    class Meta:
        db_table = 'tradesbyplatform'


class VolumeByPlatform(models.Model):
    time = models.DateTimeField()
    platform = models.CharField(max_length=100)
    volume = models.DecimalField(max_digits=20, decimal_places=8)
    objects = models.Manager()

    class Meta:
        db_table = 'volumebyplatform'


class GasFeesData(models.Model):
    time = models.DateTimeField()
    ethereum_gas_usd = models.DecimalField(max_digits=12, decimal_places=9)
    polygon_gas_usd = models.DecimalField(max_digits=12, decimal_places=9)
    arbitrum_gas_usd = models.DecimalField(max_digits=12, decimal_places=9)
    optimism_gas_usd = models.DecimalField(max_digits=12, decimal_places=9)
    objects = models.Manager()

    class Meta:
        db_table = 'gasfeesdata'


class AvgFees(models.Model):
    day = models.DateTimeField()
    avg_fee_per_transactions = models.DecimalField(max_digits=10, decimal_places=3)
    objects = models.Manager()

    class Meta:
        db_table = 'avgfees'


class EthereumNFTCollections(models.Model):
    highest_sales = models.DecimalField(max_digits=10, decimal_places=3)
    lowest_sales = models.DecimalField(max_digits=10, decimal_places=3)
    collection = models.CharField(max_length=100)
    etherscan_link = models.URLField(max_length=200)
    owners = models.IntegerField()
    supply = models.IntegerField()
    blur_link = models.URLField(max_length=200)
    gem_link = models.URLField(max_length=200)
    uniswap_link = models.URLField(max_length=200)
    objects = models.Manager()

    class Meta:
        db_table = 'ethereum_nft_collections'
