import time
from kite_market_data import update_candles
from strategy import calculate_vwap, check_vwap_retest
from telegram_bot import send_test

RELIANCE_TOKEN = 738561

print("Bot started in PAPER mode (Zerodha live quotes)")

while True:
    try:
        df = update_candles(RELIANCE_TOKEN)
        df = calculate_vwap(df)

        signal = check_vwap_retest(df)

        if signal:
            send_test()
            print("PAPER signal sent")

        time.sleep(30)  # poll quotes every 30 sec

    except Exception as e:
        print("Error:", e)
        time.sleep(30)
