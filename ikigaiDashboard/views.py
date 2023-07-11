from rest_framework.decorators import api_view
from django.http import JsonResponse
from .models import NFTSales, EthereumTraders, BTCTraders, AvgFees, BtcUsersData, EthereumWallets, GasFeesData
from .serializers import NFTSalesSerializer, EthereumTradersSerializer, BtcTradersSerializer, AvgFeesSerializer, \
    BtcUsersDataSerializer, EthereumWalletsSerializer, GasFeesDataSerializer


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


@api_view(['GET'])
def avg_fees_api(request):
    avg_fees = AvgFees.objects.all()
    serializer = AvgFeesSerializer(avg_fees, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def btc_users_data_api(request):
    btc_users_data = BtcUsersData.objects.all()
    serializer = BtcUsersDataSerializer(btc_users_data, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def ethereum_wallets_api(request):
    ethereum_wallets = EthereumWallets.objects.all()
    serializer = EthereumWalletsSerializer(ethereum_wallets, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def gas_fees_data_api(request):
    gas_fees_data = GasFeesData.objects.all()
    serializer = GasFeesDataSerializer(gas_fees_data, many=True)
    return JsonResponse(serializer.data, safe=False)