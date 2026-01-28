from kiteconnect import KiteTicker
import os
import pandas as pd
from datetime import datetime

API_KEY = os.getenv("KITE_API_KEY")
ACCESS_TOKEN = os.getenv("KITE_ACCESS_TOKEN")

# RELIANCE instrument token
INSTRUMENT_TOKEN = 738561

# store ticks → candles
ticks_buffer = []
candles = []

def build_5min_candle(price, volume, timestamp):
    global candles

    candle_time = timestamp.replace(
        minute=(timestamp.minute // 5) * 5,
        second=0,
        microsecond=0
    )

    if candles and candles[-1]["time"] == candle_time:
        c = candles[-1]
        c["high"] = max(c["high"], price)
        c["low"] = min(c["low"], price)
        c["close"] = price
        c["volume"] += volume
    else:
        candles.append({
            "time": candle_time,
            "open": price,
            "high": price,
            "low": price,
            "close": price,
            "volume": volume
        })

    return pd.DataFrame(candles[-20:])

def start_ticker(on_candle_close):
    kws = KiteTicker(API_KEY, ACCESS_TOKEN)

    def on_ticks(ws, ticks):
        for t in ticks:
            price = t["last_price"]
            volume = t.get("volume_traded", 0)
            ts = t["exchange_timestamp"] or datetime.now()

            df = build_5min_candle(price, volume, ts)
            on_candle_close(df)

    def on_connect(ws, response):
        ws.subscribe([INSTRUMENT_TOKEN])
        ws.set_mode(ws.MODE_LTP, [INSTRUMENT_TOKEN])
        print("KiteTicker connected")

    def on_close(ws, code, reason):
        print("KiteTicker closed", reason)

    kws.on_ticks = on_ticks
    kws.on_connect = on_connect
    kws.on_close = on_close

    kws.connect(threaded=False)