import time
from kite_market_data import get_5min_candles
from strategy import calculate_vwap, check_vwap_retest
from telegram_bot import send_test

# Zerodha instrument token
RELIANCE_TOKEN = 738561

print("Bot started in PAPER mode (Zerodha live data)")

while True:
    try:
        df = get_5min_candles(RELIANCE_TOKEN)
        df = calculate_vwap(df)

        signal = check_vwap_retest(df)

        if signal:
            send_test()
            print("PAPER signal sent")

        time.sleep(300)  # 5 minutes

    except Exception as e:
        print("Error:", e)
        time.sleep(60)