import requests
from ikigaiDashboard.models import NFTSales, EthereumTraders, BTCTraders, AvgFees, BtcUsersData, EthereumWallets, \
    GasFeesData, NftLowestSalePrices, NftTradesByChain, EthereumL2Transactions, \
    VolumeByPlatform, BitcoinTransaction, TradesByPlatform, EthereumNFTCollections
from datetime import datetime
from django.utils import timezone
from bs4 import BeautifulSoup


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


def fetch_and_store_nft_lowest_sale_prices():
    api_url = 'https://api.dune.com/api/v1/query/2647766/results?api_key=piyMny0VjuHCs1Mk5KLTXCwOpclpXcvQ'
    date_format = "%Y-%m-%d %H:%M:%S.%f %Z"

    # Fetch data from the API
    response = requests.get(api_url)
    response.raise_for_status()

    # Parse the JSON response
    data = response.json()

    # Extract the relevant data from the response
    rows = data['result']['rows']

    # Iterate through each row and create NftLowestSalePrices object if not exists
    for row in rows:
        naive_time = datetime.strptime(row['time'], date_format)
        aware_time = timezone.make_aware(naive_time, timezone.utc)
        name = row['name']
        lowest_sale_price = row['Lowest_sale_price']
        current_floor = row['current_floor']

        # Get or create NftLowestSalePrices object
        NftLowestSalePrices.objects.get_or_create(
            time=aware_time,
            name=name,
            defaults={'lowest_sale_price': lowest_sale_price, 'current_floor': current_floor}
        )


def fetch_and_store_nft_trades_by_chain():
    api_url = 'https://api.dune.com/api/v1/query/2514217/results?api_key=piyMny0VjuHCs1Mk5KLTXCwOpclpXcvQ'
    date_format = "%Y-%m-%d %H:%M:%S.%f %Z"

    # Fetch data from the API
    response = requests.get(api_url)
    response.raise_for_status()

    # Parse the JSON response
    data = response.json()

    # Extract the relevant data from the response
    rows = data['result']['rows']

    # Iterate through each row and create NftTradesByChain object if not exists
    for row in rows:
        naive_time = datetime.strptime(row['time'], date_format)
        aware_time = timezone.make_aware(naive_time, timezone.utc)
        chain = row['chain']
        number_of_trades = row['number_of_trades']

        # Get or create NftTradesByChain object
        NftTradesByChain.objects.get_or_create(
            time=aware_time,
            chain=chain,
            defaults={'number_of_trades': number_of_trades}
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
            date=aware_date,
            project=project,
            defaults={'trades': trades}
        )


def fetch_and_store_bitcoin_transactions():
    api_url = 'https://api.dune.com/api/v1/query/2526230/results?api_key=piyMny0VjuHCs1Mk5KLTXCwOpclpXcvQ'
    date_format = "%Y-%m-%d"

    # Fetch data from the API
    response = requests.get(api_url)
    response.raise_for_status()

    # Parse the JSON response
    data = response.json()

    # Extract the relevant data from the response
    rows = data['result']['rows']

    # Iterate through each row and create BitcoinTransaction object if not exists
    for row in rows:
        day = datetime.strptime(row['Day'], date_format).date()
        non_odrdinal_tx = row['non_Odrdinal_Tx']
        brc20_tx = row['BRC20_Tx']
        non_brc20_ordi_tx = row['non_BRC20_Ordi_Tx']
        non_odrdinal_fee = row['non_Odrdinal_Fee']
        brc20_fee = row['BRC20_Fee']
        non_brc20_ordi_fee = row['non_BRC20_Ordi_Fee']

        # Get or create BitcoinTransaction object
        BitcoinTransaction.objects.get_or_create(
            day=day,
            defaults={
                'non_odrdinal_tx': non_odrdinal_tx,
                'brc20_tx': brc20_tx,
                'non_brc20_ordi_tx': non_brc20_ordi_tx,
                'non_odrdinal_fee': non_odrdinal_fee,
                'brc20_fee': brc20_fee,
                'non_brc20_ordi_fee': non_brc20_ordi_fee
            }
        )


def fetch_and_store_ethereum_l2_transactions():
    api_url = 'https://api.dune.com/api/v1/query/2632324/results?api_key=piyMny0VjuHCs1Mk5KLTXCwOpclpXcvQ'
    date_format = "%Y-%m-%d %H:%M:%S.%f %Z"

    # Fetch data from the API
    response = requests.get(api_url)
    response.raise_for_status()

    # Parse the JSON response
    data = response.json()

    # Extract the relevant data from the response
    rows = data['result']['rows']

    # Iterate through each row and create EthereumL2Transactions object if not exists
    for row in rows:
        naive_time = datetime.strptime(row['time'], date_format)
        aware_time = timezone.make_aware(naive_time, timezone.utc)
        ethereum_transactions = row['ethereum_transactions']
        polygon_transactions = row['polygon_transactions']
        arbitrum_transactions = row['arbitrum_transactions']
        optimism_transactions = row['optimism_transactions']

        # Get or create EthereumL2Transactions object
        EthereumL2Transactions.objects.get_or_create(
            time=aware_time,
            defaults={
                'ethereum_transactions': ethereum_transactions,
                'polygon_transactions': polygon_transactions,
                'arbitrum_transactions': arbitrum_transactions,
                'optimism_transactions': optimism_transactions
            }
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


# Define a function to fetch and store the NFT collections data
def fetch_and_store_nft_collections():
    # The URL of the API endpoint
    api_url = 'https://api.dune.com/api/v1/query/2720612/results?api_key=piyMny0VjuHCs1Mk5KLTXCwOpclpXcvQ'

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
        # Parse the HTML string in the 'collection' and 'trade_there' field using BeautifulSoup
        collection_html = BeautifulSoup(row['collection'], 'html.parser')
        trade_there_html = BeautifulSoup(row['trade_there'], 'html.parser')

        # Create a new EthereumNFTCollections object or update an existing one
        # 'get_or_create' will avoid duplicate entries if called multiple times with same data
        EthereumNFTCollections.objects.get_or_create(
            highest_sales=row['Highest_sales'],
            lowest_sales=row['Lowest_sales'],
            collection=collection_html.text,  # Extract the text (name) of the collection
            etherscan_link=collection_html.find('a')['href'],
            # Extract the href attribute of the first (and only) anchor tag in the 'collection' field
            owners=row['owners'],
            supply=row['supply'],
            blur_link=trade_there_html.find_all('a')[0]['href'],
            # Extract the href attribute of the first anchor tag in the 'trade_there' field
            gem_link=trade_there_html.find_all('a')[1]['href'],
            # Extract the href attribute of the second anchor tag in the 'trade_there' field
            uniswap_link=trade_there_html.find_all('a')[2]['href'],
            # Extract the href attribute of the third anchor tag in the 'trade_there' field
        )


def fetch_and_store_data():
    # Call the functions to fetch and store data from both APIs
    # fetch_and_store_nft_sales()
    # fetch_and_store_ethereum_trade()
    # fetch_btc_trades_data()
    # fetch_and_store_avg_fees()
    # fetch_and_store_btc_users_data()
    # fetch_and_store_ethereum_wallets()
    # fetch_and_store_gas_fees_data()
    # fetch_and_store_nft_lowest_sale_prices()
    # fetch_and_store_nft_trades_by_chain()
    # fetch_and_store_trades_by_platform()
    # fetch_and_store_bitcoin_transactions()
    # fetch_and_store_ethereum_l2_transactions()
    # fetch_and_store_volume_by_platform()
    fetch_and_store_nft_collections()
