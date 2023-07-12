from rest_framework import serializers
from .models import BTCTraders, AvgFees, GasFeesData, \
    VolumeByPlatform, TradesByPlatform, EthereumNFTCollections, EthereumTraders


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


class GasFeesDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = GasFeesData
        fields = '__all__'


class TradesByPlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = TradesByPlatform
        fields = '__all__'


class VolumeByPlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = VolumeByPlatform
        fields = '__all__'


class EthereumNFTCollectionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EthereumNFTCollections
        fields = '__all__'
