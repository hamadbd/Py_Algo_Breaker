import oandapyV20
from oandapyV20 import API
import oandapyV20.endpoints.pricing as pricing
import oandapyV20.endpoints.orders as orders
import time
import pandas as pd


# Set up the API client
api = API(access_token="your_access_token")

# Set the account ID, symbol, and area boundaries
account_id = "your_account_id"
symbol = "EUR_USD"
area_boundary_low = 1.1000
area_boundary_high = 1.1500

# Initialize variables for tracking prices and trades
last_new_low = None
last_new_high = None
stop_loss = None
position = None


def calcualte_amount_to_risk(x):
    money_to_risk = 100
    risk = money_to_risk/(high)

def BOS:
    (df['high'].shift(1) < df['rolling_low'].shift(1)) and (df['high'] > df['rolling_low']):
    # Place a buy order
    amount = calculate_amount_to_risk(1)
    order = api.create_order(account_id, symbol, buy=amount, stopLoss=last_new_low)

while True:
    # Get the current pricing for the symbol
    r = pricing.PricingInfo(accountID=account_id, instruments=symbol)
    pricing_info = api.request(r)
    current_price = float(pricing_info['prices'][0]['closeoutBid'])

    # Check if the current price is within the defined area
    if area_boundary_low <= current_price <= area_boundary_high:
        if area_boundary_low <= current_price:
            # Condition A: area was lower than current price
            # Check for a break of structure to the upside
            if  (df['high'].shift(1) < df['rolling_low'].shift(1)) and (df['high'] > df['rolling_low']):
                # Place a buy order
                amount = calculate_amount_to_risk(1)
                order = api.create_order(account_id, symbol, buy=amount, stopLoss=last_new_low)
                print("Buy order placed at ", order['price'])
                position = "long"
                last_new_low = current_price
                stop_loss = last_new_low - (last_new_high - last_new_low)
        elif area_boundary_high >= current_price:
            # Condition B: area was higher than current price
            # Check for a break of structure to the downside
            if BOS:
                # Place a sell order
                amount = calculate_amount_to_risk(1)
                order = api.create_order(account_id, symbol, sell=amount, stopLoss=last_new_high)
                print("Sell order placed at ", order['price'])
                position = "short"
                last_new_high = current_price
                stop_loss = last_new_high + (last_new_high - last_new_low)