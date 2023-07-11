import requests
from ikigaiDashboard.models import NFTSales, EthereumTraders, BTCTraders, AvgFees, BtcUsersData, EthereumWallets, \
    GasFeesData
from datetime import datetime
from django.utils import timezone


def fetch_and_store_nft_sales():
    api_url = 'https://api.dune.com/api/v1/query/2651564/results?api_key=piyMny0VjuHCs1Mk5KLTXCwOpclpXcvQ'
    date_format = "%Y-%m-%d %H:%M:%S.%f %Z"

    # Fetch data from the API
    response = requests.get(api_url)
    response.raise_for_status()

    # Parse the JSON response
    data = response.json()

    # Extract the relevant data from the response
    rows = data['result']['rows']

    # Iterate through each row and create NFTSales object if not exists
    for row in rows:
        naive_time = datetime.strptime(row['time'], date_format)
        aware_time = timezone.make_aware(naive_time, timezone.utc)
        name = row['name']
        highest_sale_price = row['Highest_sale_price']
        current_floor = row['current_floor']

        # Get or create NFTSales object
        NFTSales.objects.get_or_create(
            time=aware_time,
            name=name,
            defaults={'highest_sale_price': highest_sale_price, 'current_floor': current_floor}
        )


def fetch_and_store_ethereum_trade():
    api_url = 'https://api.dune.com/api/v1/query/2192307/results?api_key=piyMny0VjuHCs1Mk5KLTXCwOpclpXcvQ'
    date_format = "%Y-%m-%d"

    # Fetch data from the API
    response = requests.get(api_url)
    response.raise_for_status()

    # Parse the JSON response
    data = response.json()

    # Extract the relevant data from the response
    rows = data['result']['rows']

    # Iterate through each row and create EthereumTraders object if not exists
    for row in rows:
        naive_date = datetime.strptime(row['Date'].split(" ")[0], date_format)
        aware_date = timezone.make_aware(naive_date, timezone.utc)
        buyers = row['Buyers']
        sellers = row['Sellers']
        unique_traders = row['Unique Traders']

        # Get or create EthereumTraders object
        EthereumTraders.objects.get_or_create(
            date=aware_date,
            defaults={'buyers': buyers, 'sellers': sellers, 'unique_traders': unique_traders}
        )


def fetch_btc_trades_data():
    api_url = 'https://api.dune.com/api/v1/query/2617886/results?api_key=piyMny0VjuHCs1Mk5KLTXCwOpclpXcvQ'
    date_format = "%Y-%m-%d %H:%M:%S.%f %Z"

    # Fetch data from the API
    response = requests.get(api_url)
    response.raise_for_status()

    # Parse the JSON response
    data = response.json()

    # Extract the relevant data from the response
    rows = data['result']['rows']

    # Iterate through each row and create BTCTraders object if not exists
    for row in rows:
        naive_date = datetime.strptime(row['date'], date_format)
        aware_date = timezone.make_aware(naive_date, timezone.utc)
        total_buyers = row['total_buyers']
        total_sellers = row['total_sellers']
        total_traders = row['total_traders']

        # Get or create BTCTraders object
        BTCTraders.objects.get_or_create(
            date=aware_date,
            defaults={'total_buyers': total_buyers, 'total_sellers': total_sellers, 'total_traders': total_traders}
        )



def fetch_and_store_avg_fees():
    api_url = 'https://api.dune.com/api/v1/query/2643482/results?api_key=piyMny0VjuHCs1Mk5KLTXCwOpclpXcvQ'
    date_format = "%Y-%m-%d %H:%M:%S.%f %Z"

    # Fetch data from the API
    response = requests.get(api_url)
    response.raise_for_status()

    # Parse the JSON response
    data = response.json()

    # Extract the relevant data from the response
    rows = data['result']['rows']

    # Iterate through each row and create AvgFees object if not exists
    for row in rows:
        naive_time = datetime.strptime(row['day'], date_format)
        aware_time = timezone.make_aware(naive_time, timezone.utc)
        avg_fee_per_transactions = row['avg_fee_per_transactions']

        # Get or create AvgFees object
        AvgFees.objects.get_or_create(
            day=aware_time,
            defaults={'avg_fee_per_transactions': avg_fee_per_transactions}
        )


def fetch_and_store_btc_users_data():
    api_url = 'https://api.dune.com/api/v1/query/2505673/results?api_key=piyMny0VjuHCs1Mk5KLTXCwOpclpXcvQ'
    date_format = "%Y-%m-%d %H:%M:%S.%f %Z"

    # Fetch data from the API
    response = requests.get(api_url)
    response.raise_for_status()

    # Parse the JSON response
    data = response.json()

    # Extract the relevant data from the response
    rows = data['result']['rows']

    # Iterate through each row and create BtcUsersData object if not exists
    for row in rows:
        naive_time = datetime.strptime(row['time'], date_format)
        aware_time = timezone.make_aware(naive_time, timezone.utc)
        users = row['users']

        # Get or create BtcUsersData object
        BtcUsersData.objects.get_or_create(
            time=aware_time,
            defaults={'users': users}
        )


def fetch_and_store_ethereum_wallets():
    api_url = 'https://api.dune.com/api/v1/query/2644593/results?api_key=piyMny0VjuHCs1Mk5KLTXCwOpclpXcvQ'
    date_format = "%Y-%m-%d %H:%M:%S.%f %Z"

    # Fetch data from the API
    response = requests.get(api_url)
    response.raise_for_status()

    # Parse the JSON response
    data = response.json()

    # Extract the relevant data from the response
    rows = data['result']['rows']

    # Iterate through each row and create EthereumWallets object if not exists
    for row in rows:
        naive_time = datetime.strptime(row['time'], date_format)
        aware_time = timezone.make_aware(naive_time, timezone.utc)
        ethereum_addresses = row['ethereum_addresses']
        polygon_addresses = row['polygon_addresses']
        arbitrum_addresses = row['arbitrum_addresses']
        optimism_addresses = row['optimism_addresses']

        # Get or create EthereumWallets object
        EthereumWallets.objects.get_or_create(
            time=aware_time,
            defaults={
                'ethereum_addresses': ethereum_addresses,
                'polygon_addresses': polygon_addresses,
                'arbitrum_addresses': arbitrum_addresses,
                'optimism_addresses': optimism_addresses
            }
        )


def fetch_and_store_gas_fees_data():
    api_url = 'https://api.dune.com/api/v1/query/2632688/results?api_key=piyMny0VjuHCs1Mk5KLTXCwOpclpXcvQ'
    date_format = "%Y-%m-%d %H:%M:%S.%f %Z"

    # Fetch data from the API
    response = requests.get(api_url)
    response.raise_for_status()

    # Parse the JSON response
    data = response.json()

    # Extract the relevant data from the response
    rows = data['result']['rows']

    # Iterate through each row and create GasFeesData object if not exists
    for row in rows:
        naive_time = datetime.strptime(row['time'], date_format)
        aware_time = timezone.make_aware(naive_time, timezone.utc)
        ethereum_gas_usd = row['ethereum_gas_usd']
        polygon_gas_usd = row['polygon_gas_usd']
        arbitrum_gas_usd = row['arbitrum_gas_usd']
        optimism_gas_usd = row['optimism_gas_usd']

        # Get or create GasFeesData object
        GasFeesData.objects.get_or_create(
            time=aware_time,
            defaults={
                'ethereum_gas_usd': ethereum_gas_usd,
                'polygon_gas_usd': polygon_gas_usd,
                'arbitrum_gas_usd': arbitrum_gas_usd,
                'optimism_gas_usd': optimism_gas_usd
            }
        )


def fetch_and_store_data():
    # Call the functions to fetch and store data from both APIs
    fetch_and_store_nft_sales()
    fetch_and_store_ethereum_trade()
    fetch_btc_trades_data()
    fetch_and_store_avg_fees()
    fetch_and_store_btc_users_data()
    fetch_and_store_ethereum_wallets()
    fetch_and_store_gas_fees_data()

