from server import app

print("Bot started in PAPER mode (TradingView)")

app.run(host="0.0.0.0", port=8000)