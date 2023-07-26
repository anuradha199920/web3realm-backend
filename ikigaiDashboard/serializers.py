from rest_framework import serializers
from .models import BTCTraders, AvgFees, GasFeesData, \
    VolumeByPlatform, TradesByPlatform, EthereumNFTCollections, EthereumTraders, NFTStats, NFTStatsByPlatform, \
    MarketOverview


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


class NFTStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NFTStats
        fields = '__all__'


class NFTStatsByPlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = NFTStatsByPlatform
        fields = '__all__'


class MarketOverviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarketOverview
        fields = '__all__'
