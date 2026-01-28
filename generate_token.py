from kiteconnect import KiteConnect

API_KEY = "sctkc2x4x8o9f9m7"
API_SECRET = "9py8sipw6h32642eghdpf0tc5ermgjxz"
REQUEST_TOKEN = "Jk309UuTdcIdG1KBWn6Ay7QWtQrqr1jx"

kite = KiteConnect(api_key=API_KEY)
data = kite.generate_session(REQUEST_TOKEN, api_secret=API_SECRET)

print("ACCESS_TOKEN =", data["access_token"])