from ticker import start_ticker
from strategy import calculate_vwap, check_vwap_retest
from telegram_bot import send_test

print("Bot started in PAPER mode (KiteTicker WebSocket)")

last_signal_time = None

def on_new_candle(df):
    global last_signal_time

    df = calculate_vwap(df)
    signal = check_vwap_retest(df)

    if signal:
        now = df.iloc[-1]["time"]
        if last_signal_time != now:
            send_test()
            print("PAPER signal sent")
            last_signal_time = now

start_ticker(on_new_candle)