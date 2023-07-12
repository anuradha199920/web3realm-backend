from django.urls import path
from .views import get_ethereum_traders, nft_sales_api, get_btc_traders, avg_fees_api, btc_users_data_api, \
    gas_fees_data_api, ethereum_wallets_api, nft_lowest_sale_prices_api, nft_trades_by_chain_api, \
    ethereum_l2_transactions_api, volume_by_platform_api, bitcoin_transaction_api, nft_collections_api

urlpatterns = [
    path('ethereum-traders/', get_ethereum_traders, name='ethereum_traders'),
    path('nft-sales/', nft_sales_api, name='nft_sales_api'),
    path('btc-traders/', get_btc_traders, name='btc_traders'),
    path('avg-fees/', avg_fees_api, name='avg_fees'),
    path('btc-users-data/', btc_users_data_api, name='btc_users_data'),
    path('ethereum-wallets/', ethereum_wallets_api, name='ethereum_wallets'),
    path('gas-fees-data/', gas_fees_data_api, name='gas_fees_data'),
    path('nft-lowest-sale-prices/', nft_lowest_sale_prices_api, name='nft_lowest_sale_prices'),
    path('nft-trades-by-chain/', nft_trades_by_chain_api, name='nft_trades_by_chain'),
    path('bitcoin-transactions/', bitcoin_transaction_api, name='bitcoin_transactions'),
    path('volume-by-platform/', volume_by_platform_api, name='volume_by_platform'),
    path('ethereum-l2-transactions/', ethereum_l2_transactions_api, name='ethereum_l2_transactions'),
    path('ethereum-nft-collections/', nft_collections_api, name='ethereum_nft_collections')
]
