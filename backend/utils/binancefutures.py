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