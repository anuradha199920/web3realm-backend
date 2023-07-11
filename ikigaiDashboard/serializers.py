from rest_framework import serializers
from .models import NFTSales, EthereumTraders, BTCTraders, AvgFees, BtcUsersData, EthereumWallets, GasFeesData


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
