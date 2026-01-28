import time
from simulated_market import get_simulated_candles
from strategy import calculate_vwap, check_vwap_retest
from telegram_bot import send_test

print("Bot started in SAFE SIMULATION mode")

while True:
    try:
        df = get_simulated_candles()
        df = calculate_vwap(df)

        signal = check_vwap_retest(df)

        if signal:
            send_test()
            print("Simulated PAPER signal sent")

        time.sleep(300)  # simulate 5-min candle

    except Exception as e:
        print("Error:", e)
        time.sleep(60)