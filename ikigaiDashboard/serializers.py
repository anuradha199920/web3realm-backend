from rest_framework import serializers
from .models import NFTSales, EthereumTraders, BTCTraders


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
