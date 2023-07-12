from rest_framework.decorators import api_view
from django.http import JsonResponse
from .models import BTCTraders, AvgFees, GasFeesData, \
    VolumeByPlatform, TradesByPlatform, EthereumNFTCollections, EthereumTraders
from .serializers import BtcTradersSerializer, AvgFeesSerializer, GasFeesDataSerializer, \
    VolumeByPlatformSerializer, TradesByPlatformSerializer, EthereumNFTCollectionsSerializer, EthereumTradersSerializer


@api_view(['GET'])
def get_ethereum_traders(request):
    ethereum_traders = EthereumTraders.objects.all()
    serializer = EthereumTradersSerializer(ethereum_traders, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def get_btc_traders(request):
    btc_traders = BTCTraders.objects.all()
    serializer = BtcTradersSerializer(btc_traders, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def avg_fees_api(request):
    avg_fees = AvgFees.objects.all()
    serializer = AvgFeesSerializer(avg_fees, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def gas_fees_data_api(request):
    gas_fees_data = GasFeesData.objects.all()
    serializer = GasFeesDataSerializer(gas_fees_data, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def trades_by_platform_api(request):
    trades_by_platform = TradesByPlatform.objects.all()
    serializer = TradesByPlatformSerializer(trades_by_platform, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def volume_by_platform_api(request):
    volume_by_platform = VolumeByPlatform.objects.all()
    serializer = VolumeByPlatformSerializer(volume_by_platform, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def nft_collections_api(request):
    nft_collections = EthereumNFTCollections.objects.all()
    serializer = EthereumNFTCollectionsSerializer(nft_collections, many=True)
    return JsonResponse(serializer.data, safe=False)