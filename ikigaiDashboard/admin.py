from django.contrib import admin
from .models import NFTSales, EthereumTraders, BTCTraders


# Register the NFTSales model
admin.site.register(NFTSales)
# Register the EthereumTraders model
admin.site.register(EthereumTraders)
# Register the BTCTraders model
admin.site.register(BTCTraders)
