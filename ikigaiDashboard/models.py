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


class NFTStats(models.Model):
    highest_sale = models.DecimalField(max_digits=10, decimal_places=3)
    lowest_sale = models.DecimalField(max_digits=10, decimal_places=3)
    buyers = models.IntegerField()
    collection = models.CharField(max_length=100)
    owners = models.IntegerField()
    sales_count= models.IntegerField()
    supply = models.IntegerField()
    sellers = models.IntegerField()
    blur_link = models.URLField(max_length=200)
    gem_link = models.URLField(max_length=200)
    uniswap_link = models.URLField(max_length=200)
    wash_volume = models.DecimalField(max_digits=20, decimal_places=8)
    wash_volume_percentage = models.DecimalField(max_digits=20, decimal_places=8)
    organic_volume = models.DecimalField(max_digits=20, decimal_places=8)
    objects = models.Manager()

    class Meta:
        db_table = 'nft_stats'


class NFTStatsByPlatform(models.Model):
    highest_sale = models.DecimalField(max_digits=10, decimal_places=3)
    buyers = models.IntegerField()
    project = models.CharField(max_length=100)
    sales_count = models.IntegerField()
    sellers = models.IntegerField()
    wash_volume = models.DecimalField(max_digits=20, decimal_places=8)
    wash_volume_percentage = models.DecimalField(max_digits=20, decimal_places=8)
    organic_volume = models.DecimalField(max_digits=20, decimal_places=8)
    date = models.DateTimeField()
    objects = models.Manager()

    class Meta:
        db_table = 'nft_stats_by_platform'


class MarketOverview(models.Model):
    highest_sale = models.DecimalField(max_digits=10, decimal_places=3)
    buyers = models.IntegerField()
    organic_volume = models.DecimalField(max_digits=20, decimal_places=8)
    sales = models.IntegerField()
    sellers = models.IntegerField()
    date = models.DateTimeField()
    wash_volume = models.DecimalField(max_digits=20, decimal_places=8)
    wash_volume_percentage = models.DecimalField(max_digits=20, decimal_places=8)
    objects = models.Manager()
    class Meta:
        db_table = 'market_overview'
