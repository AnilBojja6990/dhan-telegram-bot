from kiteconnect import KiteConnect
import pandas as pd
import os

API_KEY = os.getenv("KITE_API_KEY")
ACCESS_TOKEN = os.getenv("KITE_ACCESS_TOKEN")

kite = KiteConnect(api_key=API_KEY)
kite.set_access_token(ACCESS_TOKEN)

def get_5min_candles(instrument_token):
    data = kite.historical_data(
        instrument_token,
        from_date=None,
        to_date=None,
        interval="5minute"
    )

    df = pd.DataFrame(data)
    return df