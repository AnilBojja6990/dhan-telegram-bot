from flask import Flask, request, jsonify
from strategy import calculate_vwap, check_vwap_retest
from telegram_bot import send_test
import pandas as pd

app = Flask(__name__)

# store candles in memory (paper mode)
candles = []

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json

    candles.append({
        "close": float(data["close"]),
        "high": float(data["high"]),
        "low": float(data["low"]),
        "volume": float(data["volume"])
    })

    # keep last 20 candles only
    if len(candles) > 20:
        candles.pop(0)

    df = pd.DataFrame(candles)
    df = calculate_vwap(df)

    signal = check_vwap_retest(df)

    if signal:
        send_test()   # later we replace message format

    return jsonify({"status": "ok"})