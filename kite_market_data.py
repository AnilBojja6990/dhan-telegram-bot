from kiteconnect import KiteConnect
import pandas as pd
import os
from datetime import datetime

kite = KiteConnect(api_key=os.getenv("KITE_API_KEY"))
kite.set_access_token(os.getenv("KITE_ACCESS_TOKEN"))

candles = []

def update_candles(symbol):
    quote = kite.quote([symbol])[symbol]

    ltp = quote["last_price"]
    volume = quote["volume"]

    now = datetime.now()
    minute = (now.minute // 5) * 5
    candle_time = now.replace(minute=minute, second=0, microsecond=0)

    if candles and candles[-1]["time"] == candle_time:
        candles[-1]["high"] = max(candles[-1]["high"], ltp)
        candles[-1]["low"] = min(candles[-1]["low"], ltp)
        candles[-1]["close"] = ltp
        candles[-1]["volume"] = volume
    else:
        candles.append({
            "time": candle_time,
            "open": ltp,
            "high": ltp,
            "low": ltp,
            "close": ltp,
            "volume": volume
        })

    return pd.DataFrame(candles[-20:])