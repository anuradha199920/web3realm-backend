from django.urls import path
from .views import get_ethereum_traders, nft_sales_api, get_btc_traders, avg_fees_api, btc_users_data_api, \
    gas_fees_data_api, ethereum_wallets_api


urlpatterns = [
    path('ethereum-traders/', get_ethereum_traders, name='ethereum_traders'),
    path('nft-sales/', nft_sales_api, name='nft_sales_api'),
    path('btc-traders/', get_btc_traders, name='btc_traders'),
    path('avg-fees/', avg_fees_api, name='avg_fees'),
    path('btc-users-data/', btc_users_data_api, name='btc_users_data'),
    path('ethereum-wallets/', ethereum_wallets_api, name='ethereum_wallets'),
    path('gas-fees-data/', gas_fees_data_api, name='gas_fees_data')
]
