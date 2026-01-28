import random
import pandas as pd

price = 81600

def get_simulated_candles():
    global price
    candles = []

    for _ in range(20):
        open_p = price
        move = random.randint(-40, 40)
        close_p = open_p + move
        high = max(open_p, close_p) + random.randint(5, 15)
        low = min(open_p, close_p) - random.randint(5, 15)
        volume = random.randint(1000, 3000)

        candles.append({
            "open": open_p,
            "high": high,
            "low": low,
            "close": close_p,
            "volume": volume
        })

        price = close_p

    return pd.DataFrame(candles)