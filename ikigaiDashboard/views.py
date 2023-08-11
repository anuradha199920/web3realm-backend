from .models import BTCTraders, AvgFees, GasFeesData, \
    VolumeByPlatform, TradesByPlatform, EthereumNFTCollections, EthereumTraders, NFTStats, NFTStatsByPlatform, \
    MarketOverview
from .serializers import BtcTradersSerializer, AvgFeesSerializer, GasFeesDataSerializer, \
    VolumeByPlatformSerializer, TradesByPlatformSerializer, EthereumNFTCollectionsSerializer, \
    NFTStatsSerializer, NFTStatsByPlatformSerializer, MarketOverviewSerializer
from .queryGenerator import get_query
from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from .models import EthereumTraders
from .serializers import EthereumTradersSerializer


# @api_view(['POST'])
# def get_query_by_text(request):
#     # Get the plain text data from the POST request
#     user_input = request.body.decode('utf-8')
#
#     return JsonResponse(get_query("Find"), status=201)  # Return a 201 Created status


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


@api_view(['GET'])
def nft_stats_api(request):
    nft_stats = NFTStats.objects.all()
    serializer = NFTStatsSerializer(nft_stats, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def nft_stats_by_platform_api(request):
    nft_stats = NFTStatsByPlatform.objects.all()
    serializer = NFTStatsByPlatformSerializer(nft_stats, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def market_overview_api(request):
    market_overview = MarketOverview.objects.all()
    serializer = MarketOverviewSerializer(market_overview, many=True)
    return JsonResponse(serializer.data, safe=False)
