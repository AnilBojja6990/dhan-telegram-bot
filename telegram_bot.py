from telegram import Bot
from config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID

bot = Bot(token=TELEGRAM_BOT_TOKEN)

def send_test():
    bot.send_message(
        chat_id=TELEGRAM_CHAT_ID,
        text="✅ Bot is LIVE on cloud"
    )