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


class AvgFees(models.Model):
    day = models.DateTimeField()
    avg_fee_per_transactions = models.DecimalField(max_digits=10, decimal_places=3)
    objects = models.Manager()

    class Meta:
        db_table = 'avgfees'


class BtcUsersData(models.Model):
    time = models.DateTimeField()
    users = models.IntegerField()
    objects = models.Manager()

    class Meta:
        db_table = 'btcusersdata'


class EthereumWallets(models.Model):
    time = models.DateTimeField()
    ethereum_addresses = models.IntegerField()
    polygon_addresses = models.IntegerField()
    arbitrum_addresses = models.IntegerField()
    optimism_addresses = models.IntegerField()
    objects = models.Manager()

    class Meta:
        db_table = 'ethereumwallets'


class GasFeesData(models.Model):
    time = models.DateTimeField()
    ethereum_gas_usd = models.DecimalField(max_digits=12, decimal_places=9)
    polygon_gas_usd = models.DecimalField(max_digits=12, decimal_places=9)
    arbitrum_gas_usd = models.DecimalField(max_digits=12, decimal_places=9)
    optimism_gas_usd = models.DecimalField(max_digits=12, decimal_places=9)
    objects = models.Manager()

    class Meta:
        db_table = 'gasfeesdata'


class NftLowestSalePrices(models.Model):
    time = models.DateTimeField()
    name = models.CharField(max_length=100)
    lowest_sale_price = models.DecimalField(max_digits=10, decimal_places=3)
    current_floor = models.DecimalField(max_digits=10, decimal_places=3)
    objects = models.Manager()

    class Meta:
        db_table = 'nft_lowest_sale_prices'


class NftTradesByChain(models.Model):
    time = models.DateTimeField()
    chain = models.CharField(max_length=50)
    number_of_trades = models.IntegerField()
    objects = models.Manager()

    class Meta:
        db_table = 'nfttradesbychain'


class TradesByPlatform(models.Model):
    time = models.DateTimeField()
    project = models.CharField(max_length=100)
    trades = models.IntegerField()
    objects = models.Manager()

    class Meta:
        db_table = 'tradesbyplatform'


class BitcoinTransaction(models.Model):
    day = models.DateField()
    non_odrdinal_tx = models.IntegerField()
    brc20_tx = models.IntegerField()
    non_brc20_ordi_tx = models.IntegerField()
    brc20_fee = models.DecimalField(max_digits=12, decimal_places=8)
    non_brc20_ordi_fee = models.DecimalField(max_digits=16, decimal_places=8)
    non_odrdinal_fee = models.DecimalField(max_digits=20, decimal_places=8)

    objects = models.Manager()
    class Meta:
        db_table = 'bitcointransaction'


class EthereumL2Transactions(models.Model):
    time = models.DateTimeField()
    ethereum_transactions = models.IntegerField()
    polygon_transactions = models.IntegerField()
    arbitrum_transactions = models.IntegerField()
    optimism_transactions = models.IntegerField()
    objects = models.Manager()

    class Meta:
        db_table = 'ethereum_l2_transactions'


class VolumeByPlatform(models.Model):
    time = models.DateTimeField()
    platform = models.CharField(max_length=100)
    volume = models.DecimalField(max_digits=20, decimal_places=8)
    objects = models.Manager()

    class Meta:
        db_table = 'volumebyplatform'
