from telegram import Bot
import yaml

# Загрузка конфигурации
with open("config/config.yaml", "r") as f:
    config = yaml.safe_load(f)

TELEGRAM_TOKEN = config["telegram_token"]
bot = Bot(token=TELEGRAM_TOKEN)

def send_telegram_message(chat_id, message):
    """Отправка сообщения в Telegram"""
    bot.send_message(chat_id=chat_id, text=message)
