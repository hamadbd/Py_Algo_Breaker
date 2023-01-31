import ccxt
import time

# Initialize the exchange object
exchange = ccxt.binance({
    'rateLimit': 2000,
    'enableRateLimit': True,
})

# Set the symbol, timeframe, and area boundaries
symbol = 'BTC/USDT'
timeframe = '1m'
area_boundary_low = 9000
area_boundary_high = 9500

# Initialize variables for tracking prices and trades
last_new_low = None
last_new_high = None
stop_loss = None
position = None

while True:
    # Get the current ticker data
    ticker = exchange.fetch_ticker(symbol)
    current_price = ticker['last']

    # Check if the current price is within the defined area
    if area_boundary_low <= current_price <= area_boundary_high:
        # Get the historical data for the symbol
        ohlcv = exchange.fetch_ohlcv(symbol, timeframe)
        # Get the last close price
        close_price = ohlcv[-1][4]
        if area_boundary_low <= current_price:
            # Condition A: area was lower than current price
            # Check for a break of structure to the upside
            if close_price > current_price:
                if position is None:
                    # Place a buy order
                    amount = 0.01
                    order = exchange.create_order(symbol, 'market', 'buy', amount)
                    print("Buy order placed at ", order['price'])
                    position = 'long'
                    last_new_low = current_price
                    stop_loss = last_new_low - (last_new_high - last_new_low)
        elif area_boundary_high >= current_price:
            # Condition B: area was higher than current price
            # Check for a break of structure to the downside
            if close_price < current_price:
                if position is None:
                    # Place a sell order
                    amount = 0.01
                    order = exchange.create_order(symbol, 'market', 'sell', amount)
                    print("Sell order placed at ", order['price'])
                    position = 'short'
                    last_new_high = current_price
                    stop_loss = last_new_high + (last_new_high - last_new_low)
    elif last_new_high is not None and current_price < last_new_high - stop_loss:
        # If the price goes below the stop loss, close the trade
        # Place a sell order
        amount = 0.01
        order = exchange.create_order(symbol, 'market', 'sell', amount)
        print("Sell order placed at ", order['price'])
        position = None
        last_new_high = None
    elif last_new_low is not None and current_price > last_new_low + stop_loss:
        # If the price goes above the stop loss, close the trade
        # Place a buy order
        amount = 0.01
        order = exchange.create_order(symbol, 'market', 'buy', amount)

