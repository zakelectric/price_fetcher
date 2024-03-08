import ccxt





def fetch_prices(symbol):
    exchanges = ['hitbtc','zonda', 'yobit', 'btcturk', 'bitmart', 'upbit','ace', 
                 'alpaca', 'ascendex',
                 'bequant', 'bigone', 'bit2c', 'bingx', 'bit2c',
                 'bitbank', 'bitbns', 'bitfinex', 'bitfinex2', 'bitflyer',
                 'bitget', 'bithumb',  'bitmex', 'bitopro',
                 'bitrue', 'bitso', 'bitstamp', 'bitvavo', 'bl3p', 
                 'blockchaincom', 'btcalpha', 'btcbox', 'btcmarkets',
                 'bybit', 'cex', 'coinbase', 'coinbasepro', 'coincheck', 'coinex',
                 'coinmate', 'coinone', 'coinsph', 'coinspot', 'cryptocom', 'currencycom',
                 'delta', 'deribit', 'digifinex', 'exmo', 'fmfwio', 'gate', 'gemini',  'hollaex',
                 'huobijp', 'idex', 'independentreserve', 'indodax', 'kraken', 'krakenfutures', 'kucoin',
                 'kuna', 'latoken', 'lbank', 'luno', 'lykke', 'mercado', 'mexc', 'ndax', 'novadax',
                 'oceanex', 'okcoin', 'okx', 'paymium', 'phemex', 'poloniex', 'poloniexfutures',
                 'probit', 'timex', 'tokocrypto', 'wavesexchange', 'wazirx', 'whitebit', 'woo', 
                 'zaif', 
                 ]
    prices = {}

    for exchange_id in exchanges:
        exchange_class = getattr(ccxt, exchange_id)
        exchange = exchange_class()

        try:
            ticker = exchange.fetch_ticker(symbol)
            price = ticker['last']  # Last traded price
            prices[exchange_id] = price
        except Exception as e:
            print(f"Could not fetch price from {exchange_id}: {e}")

    return prices


symbol = 'DOGE/USDT'
prices = fetch_prices(symbol)

sorted_prices = sorted(prices.items(), key=lambda x: float('inf') if x[1] is None else x[1])

for exchange, price in sorted_prices:
    print(f"{exchange}: {price}")
