import time
from market_data import get_dummy_candles
from strategy import calculate_vwap, check_vwap_retest
from telegram_bot import send_test
from config import MODE

print("Bot started in", MODE, "mode")

while True:
    try:
        df = get_dummy_candles()
        df = calculate_vwap(df)

        signal = check_vwap_retest(df)

        if signal and MODE == "PAPER":
            send_test()
            print("Paper signal sent")

        time.sleep(60)  # check once per minute

    except Exception as e:
        print("Error:", e)
        time.sleep(60)