def calculate_vwap(df):
    pv = (df["close"] * df["volume"]).cumsum()
    vol = df["volume"].cumsum()
    df["vwap"] = pv / vol
    return df

def check_vwap_retest(df):
    last = df.iloc[-1]
    prev = df.iloc[-2]

    if last.close > last.vwap and prev.low <= prev.vwap:
        return "CE"

    if last.close < last.vwap and prev.high >= prev.vwap:
        return "PE"

    return None