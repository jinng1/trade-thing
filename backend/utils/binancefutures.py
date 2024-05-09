import os
from binance.um_futures import UMFutures
import ta
import pandas as pd
from binance.error import ClientError

api = os.getenv('BINANCE_API_KEY')
secret = os.getenv('BINANCE_SECRET_KEY')

# initiate binance client
client = UMFutures(key=api, secret=secret)

# trade variables
tp = 0.01
sl = 0.01
volume = 50
leverage = 10
type = 'CROSS'

# get balance
def get_balance():
    try:
        response = client.balance(recvWindow=6000)
        for elem in response:
            if elem['asset'] == 'USDT':
                return float(elem['availableBalance'])
    except ClientError as error:
        print(
            "Found error. status: {}, error code: {}, error message: {}".format(
                error.status_code, error.error_code, error.error_message
            )
        )

def get_tickers():
    try:
        tickers = []
        resp = client.ticker_price()
        for elem in resp:
            if 'USDT' in elem['symbol']:
                tickers.append(elem['symbol'])
        return tickers
    except ClientError as error:
        print(
            "Found error. status: {}, error code: {}, error message: {}".format(
                error.status_code, error.error_code, error.error_message
            )
        )

def get_positions():
    try:
        resp = client.get_position_risk()
        positions = 0
        for elem in resp:
            if float(elem['positionAmt']) != 0:
                positions += 1
        return positions
    except ClientError as error:
        print(
            "Found error. status: {}, error code: {}, error message: {}".format(
                error.status_code, error.error_code, error.error_message
            )
        )