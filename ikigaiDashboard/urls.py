from django.urls import path
from .views import get_btc_traders, avg_fees_api, \
    gas_fees_data_api, volume_by_platform_api, nft_collections_api, trades_by_platform_api, get_ethereum_traders

urlpatterns = [
    path('ethereum-traders/', get_ethereum_traders, name='ethereum_traders'),
    path('btc-traders/', get_btc_traders, name='btc_traders'),
    path('avg-fees/', avg_fees_api, name='avg_fees'),
    path('trades-by-platform/',trades_by_platform_api, name='trades_by_platform'),
    path('gas-fees-data/', gas_fees_data_api, name='gas_fees_data'),
    path('volume-by-platform/', volume_by_platform_api, name='volume_by_platform'),
    path('ethereum-nft-collections/', nft_collections_api, name='ethereum_nft_collections')
]
