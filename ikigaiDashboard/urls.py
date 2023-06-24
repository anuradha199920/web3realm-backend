from django.urls import path
from .views import get_ethereum_traders, nft_sales_api, get_btc_traders

urlpatterns = [
    path('ethereum-traders/', get_ethereum_traders, name='ethereum_traders'),
    path('nft-sales/', nft_sales_api, name='nft_sales_api'),
    path('btc-traders/', get_btc_traders, name='btc_traders')
]
