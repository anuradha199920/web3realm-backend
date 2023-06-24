from rest_framework.decorators import api_view
from django.http import JsonResponse
from .models import NFTSales, EthereumTraders, BTCTraders
from .serializers import NFTSalesSerializer, EthereumTradersSerializer, BtcTradersSerializer


@api_view(['GET'])
def get_ethereum_traders(request):
    ethereum_traders = EthereumTraders.objects.all()
    serializer = EthereumTradersSerializer(ethereum_traders, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def nft_sales_api(request):
    nft_sales = NFTSales.objects.all()
    serializer = NFTSalesSerializer(nft_sales, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def get_btc_traders(request):
    btc_traders = BTCTraders.objects.all()
    serializer = BtcTradersSerializer(btc_traders, many=True)
    return JsonResponse(serializer.data, safe=False)
