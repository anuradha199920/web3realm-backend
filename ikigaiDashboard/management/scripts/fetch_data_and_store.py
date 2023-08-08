import requests
from ikigaiDashboard.models import BTCTraders, AvgFees, GasFeesData, \
    VolumeByPlatform, TradesByPlatform, EthereumTraders, NFTStats, NFTStatsByPlatform, MarketOverview
from datetime import datetime
from django.utils import timezone
from bs4 import BeautifulSoup


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
        naive_date = datetime.strptime(row['time'].split(" ")[0], date_format)
        aware_date = timezone.make_aware(naive_date, timezone.utc)
        buyers = row['buyers']
        sellers = row['sellers']
        traders = row['traders']

        # Get or create EthereumTraders object
        EthereumTraders.objects.get_or_create(
            date=aware_date,
            defaults={'buyers': buyers, 'sellers': sellers, 'traders': traders}
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


def fetch_and_store_trades_by_platform():
    api_url = 'https://api.dune.com/api/v1/query/2646974/results?api_key=piyMny0VjuHCs1Mk5KLTXCwOpclpXcvQ'
    date_format = "%Y-%m-%d %H:%M:%S.%f %Z"

    # Fetch data from the API
    response = requests.get(api_url)
    response.raise_for_status()

    # Parse the JSON response
    data = response.json()

    # Extract the relevant data from the response
    rows = data['result']['rows']

    # Iterate through each row and create TradesByPlatform object if not exists
    for row in rows:
        naive_date = datetime.strptime(row['time'], date_format)
        aware_date = timezone.make_aware(naive_date, timezone.utc)
        project = row['project']
        trades = row['trades']

        # Get or create TradesByPlatform object
        TradesByPlatform.objects.get_or_create(
            time=aware_date,
            project=project,
            defaults={'trades': trades}
        )


def fetch_and_store_volume_by_platform():
    api_url = 'https://api.dune.com/api/v1/query/2647026/results?api_key=piyMny0VjuHCs1Mk5KLTXCwOpclpXcvQ'
    date_format = "%Y-%m-%d %H:%M:%S.%f %Z"

    # Fetch data from the API
    response = requests.get(api_url)
    response.raise_for_status()

    # Parse the JSON response
    data = response.json()

    # Extract the relevant data from the response
    rows = data['result']['rows']

    # Iterate through each row and create VolumeByPlatform object if not exists
    for row in rows:
        naive_time = datetime.strptime(row['time'], date_format)
        aware_time = timezone.make_aware(naive_time, timezone.utc)
        platform = row['platform']
        volume = row['volume']

        # Get or create VolumeByPlatform object
        VolumeByPlatform.objects.get_or_create(
            time=aware_time,
            platform=platform,
            defaults={'volume': volume}
        )


# Define a function to fetch and store the NFT stats data

def fetch_and_store_nft_stats():
    # The URL of the API endpoint
    api_url = 'https://api.dune.com/api/v1/query/2774925/results?api_key=%20piyMny0VjuHCs1Mk5KLTXCwOpclpXcvQ'

    # Send a GET request to the API endpoint
    response = requests.get(api_url)
    # If the GET request is unsuccessful, raise an HTTPError
    response.raise_for_status()

    # Parse the JSON response from the API
    data = response.json()

    # Extract the 'rows' array from the 'result' object in the response
    rows = data['result']['rows']

    # Iterate over each object (row) in the 'rows' array
    for row in rows:
        # Parse the HTML string in the 'trade_there' field using BeautifulSoup
        trade_there_html = BeautifulSoup(row['trade_there'], 'html.parser')
        # Create a new NFTStats object or update an existing one
        # 'get_or_create' will avoid duplicate entries if called multiple times with same data
        NFTStats.objects.get_or_create(
            highest_sale=row['Highest_Sale'],
            lowest_sale=row['Lowest_Sale'],
            buyers=row['buyers'],
            collection=row['collection'],
            owners=row['owners'],
            sales_count=row['sales'],
            supply=row['supply'],
            sellers=row['sellers'],
            blur_link=trade_there_html.find_all('a')[0]['href'],
            # Extract the href attribute of the first anchor tag in the 'trade_there' field
            gem_link=trade_there_html.find_all('a')[1]['href'],
            # Extract the href attribute of the second anchor tag in the 'trade_there' field
            uniswap_link=trade_there_html.find_all('a')[2]['href'],
            # Extract the href attribute of the third anchor tag in the 'trade_there' field
            organic_volume=row['organic_volume'],
            wash_volume=row['wash_volume'],
            wash_volume_percentage=row['wash_volume_percentage']
        )


def fetch_and_store_nft_stats_by_platform():
    # The URL of the API endpoint
    api_url = 'https://api.dune.com/api/v1/query/2772645/results?api_key=%20piyMny0VjuHCs1Mk5KLTXCwOpclpXcvQ'
    date_format = "%Y-%m-%d %H:%M:%S.%f %Z"
    # Send a GET request to the API endpoint
    response = requests.get(api_url)
    # If the GET request is unsuccessful, raise an HTTPError
    response.raise_for_status()

    # Parse the JSON response from the API
    data = response.json()

    # Extract the 'rows' array from the 'result' object in the response
    rows = data['result']['rows']

    # Iterate over each object (row) in the 'rows' array
    for row in rows:
        naive_time = datetime.strptime(row['time'], date_format)
        aware_time = timezone.make_aware(naive_time, timezone.utc)
        NFTStatsByPlatform.objects.get_or_create(
            highest_sale=row['Highest_Sale'],
            buyers=row['buyers'],
            project=row['project'],
            sales_count=row['sales'],
            sellers=row['sellers'],
            organic_volume=row['organic_volume'],
            wash_volume=row['wash_volume'],
            wash_volume_percentage=row['wash_volume_percentage'],
            date=aware_time
        )


def fetch_and_store_market_overview():
    # The URL of the API endpoint
    api_url = 'https://api.dune.com/api/v1/query/2775171/results?api_key=%20piyMny0VjuHCs1Mk5KLTXCwOpclpXcvQ'
    date_format = "%Y-%m-%d %H:%M:%S.%f %Z"
    # Send a GET request to the API endpoint
    response = requests.get(api_url)
    # If the GET request is unsuccessful, raise an HTTPError
    response.raise_for_status()

    # Parse the JSON response from the API
    data = response.json()

    # Extract the 'rows' array from the 'result' object in the response
    rows = data['result']['rows']

    # Iterate over each object (row) in the 'rows' array
    for row in rows:
        naive_time = datetime.strptime(row['time'], date_format)
        aware_time = timezone.make_aware(naive_time, timezone.utc)
        MarketOverview.objects.get_or_create(
            highest_sale=row['Highest_Sale'],
            buyers=row['buyers'],
            organic_volume=row['organic_volume'],
            sales=row['sales'],
            sellers=row['sellers'],
            wash_volume=row['wash_volume'],
            wash_volume_percentage=row['wash_volume_percentage'],
            date=aware_time
        )


def fetch_and_store_data():
    # Call the functions to fetch and store data from both APIs
    # fetch_and_store_ethereum_trade()
    # fetch_btc_trades_data()
    # fetch_and_store_avg_fees()
    # fetch_and_store_gas_fees_data()
    # fetch_and_store_trades_by_platform()
    fetch_and_store_volume_by_platform()
    fetch_and_store_nft_stats()
    fetch_and_store_market_overview()
    fetch_and_store_nft_stats_by_platform()
