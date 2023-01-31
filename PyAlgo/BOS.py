import pandas as pd

# Create a dataframe with the price data
df = pd.DataFrame(price_data)

# Calculate the rolling high and low
df['rolling_high'] = df['high'].rolling(window=n).max()
df['rolling_low'] = df['low'].rolling(window=n).min()

# Check for a BOS to the upside
if (df['high'].shift(1) < df['rolling_low'].shift(1)) and (df['high'] > df['rolling_low']):
    # Place a buy order
    print("Buy order placed at ", df['high'].iloc[-1])



def BOS:
    (df['high'].shift(1) < df['rolling_low'].shift(1)) and (df['high'] > df['rolling_low']):
    # Place a buy order
    amount = calculate_amount_to_risk(1)
    order = api.create_order(account_id, symbol, buy=amount, stopLoss=last_new_low)
