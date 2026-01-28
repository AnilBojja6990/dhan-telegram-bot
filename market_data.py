import pandas as pd

def get_dummy_candles():
    # Temporary dummy data (we replace with real data later)
    data = {
        "close": [81500, 81540, 81520, 81580, 81610],
        "low":   [81480, 81510, 81490, 81540, 81590],
        "high":  [81530, 81570, 81560, 81600, 81640],
        "volume":[1200, 1300, 1250, 1400, 1600]
    }
    return pd.DataFrame(data)