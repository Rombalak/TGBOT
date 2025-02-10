import logging
import yaml
from src.whatsapp_api import send_whatsapp_message

# Загрузка конфигурации
with open("config/config.yaml", "r") as f:
    config = yaml.safe_load(f)

MONITORED_WHATSAPP_NUMBERS = config["monitored_whatsapp_numbers"]
MONITORED_TELEGRAM_GROUPS = config["monitored_telegram_groups"]

def handle_telegram_message(update, context):
    chat_id = update.message.chat_id
    text = update.message.text
    user = update.message.from_user.username or update.message.from_user.first_name

    logging.info(f"Received from Telegram [{user}]: {text}")

    if chat_id in MONITORED_TELEGRAM_GROUPS:
        send_whatsapp_message(MONITORED_WHATSAPP_NUMBERS[0], text)

def handle_whatsapp_message(update, context):
    args = context.args
    if len(args) < 2:
        update.message.reply_text("Использование: /whatsapp +номер сообщение")
        return
    
    number = args[0]
    message = " ".join(args[1:])
    
    if number in MONITORED_WHATSAPP_NUMBERS:
        send_whatsapp_message(number, message)
        update.message.reply_text(f"Сообщение отправлено в WhatsApp: {message}")
