from rest_framework import serializers
from .models import NFTSales, EthereumTraders, BTCTraders, AvgFees, BtcUsersData, EthereumWallets, GasFeesData, \
    NftLowestSalePrices, NftTradesByChain, EthereumL2Transactions, \
    VolumeByPlatform, BitcoinTransaction, TradesByPlatform


class NFTSalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = NFTSales
        fields = '__all__'


class EthereumTradersSerializer(serializers.ModelSerializer):
    class Meta:
        model = EthereumTraders
        fields = '__all__'


class BtcTradersSerializer(serializers.ModelSerializer):
    class Meta:
        model = BTCTraders
        fields = '__all__'


class AvgFeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AvgFees
        fields = '__all__'


class BtcUsersDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = BtcUsersData
        fields = '__all__'


class EthereumWalletsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EthereumWallets
        fields = '__all__'


class GasFeesDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = GasFeesData
        fields = '__all__'


class NftLowestSalePricesSerializer(serializers.ModelSerializer):
    class Meta:
        model = NftLowestSalePrices
        fields = '__all__'


class NftTradesByChainSerializer(serializers.ModelSerializer):
    class Meta:
        model = NftTradesByChain
        fields = '__all__'


class TradesByPlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = TradesByPlatform
        fields = '__all__'


class BitcoinTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = BitcoinTransaction
        fields = '__all__'


class EthereumL2TransactionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EthereumL2Transactions
        fields = '__all__'


class VolumeByPlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = VolumeByPlatform
        fields = '__all__'
