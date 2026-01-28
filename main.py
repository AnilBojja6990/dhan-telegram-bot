import time
from kite_market_data import update_candles
from strategy import calculate_vwap, check_vwap_retest
from telegram_bot import send_test

SYMBOL = "NSE:RELIANCE"

print("Bot started in PAPER mode (Zerodha live quotes)")

while True:
    try:
        df = update_candles(SYMBOL)
        df = calculate_vwap(df)

        signal = check_vwap_retest(df)

        if signal:
            send_test()
            print("PAPER signal sent")

        time.sleep(30)

    except Exception as e:
        print("Error:", e)
        time.sleep(30)