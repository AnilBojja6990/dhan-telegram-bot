from market_data import get_dummy_candles
from strategy import calculate_vwap, check_vwap_retest
from telegram_bot import send_test
from config import MODE

df = get_dummy_candles()
df = calculate_vwap(df)

signal = check_vwap_retest(df)

if signal and MODE == "PAPER":
    send_test()