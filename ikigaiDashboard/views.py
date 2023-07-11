from rest_framework.decorators import api_view
from django.http import JsonResponse
from .models import NFTSales, EthereumTraders, BTCTraders, AvgFees, BtcUsersData, EthereumWallets, GasFeesData, \
    NftLowestSalePrices, NftTradesByChain, EthereumL2Transactions, \
    VolumeByPlatform, BitcoinTransaction, TradesByPlatform
from .serializers import NFTSalesSerializer, EthereumTradersSerializer, BtcTradersSerializer, AvgFeesSerializer, \
    BtcUsersDataSerializer, EthereumWalletsSerializer, GasFeesDataSerializer, NftLowestSalePricesSerializer, \
    NftTradesByChainSerializer, \
    EthereumL2TransactionsSerializer, VolumeByPlatformSerializer, BitcoinTransactionSerializer, \
    TradesByPlatformSerializer


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


@api_view(['GET'])
def nft_lowest_sale_prices_api(request):
    nft_lowest_sale_prices = NftLowestSalePrices.objects.all()
    serializer = NftLowestSalePricesSerializer(nft_lowest_sale_prices, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def nft_trades_by_chain_api(request):
    nft_trades_by_chain = NftTradesByChain.objects.all()
    serializer = NftTradesByChainSerializer(nft_trades_by_chain, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def trades_by_platform_api(request):
    trades_by_platform = TradesByPlatform.objects.all()
    serializer = TradesByPlatformSerializer(trades_by_platform, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def bitcoin_transaction_api(request):
    bitcoin_transactions = BitcoinTransaction.objects.all()
    serializer = BitcoinTransactionSerializer(bitcoin_transactions, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def ethereum_l2_transactions_api(request):
    ethereum_l2_transactions = EthereumL2Transactions.objects.all()
    serializer = EthereumL2TransactionsSerializer(ethereum_l2_transactions, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def volume_by_platform_api(request):
    volume_by_platform = VolumeByPlatform.objects.all()
    serializer = VolumeByPlatformSerializer(volume_by_platform, many=True)
    return JsonResponse(serializer.data, safe=False)
