# -*- coding: utf-8 -*-

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import logging
import yaml
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
from src.whatsapp_api import send_whatsapp_message
from src.handlers import handle_telegram_message, handle_whatsapp_message

# Настройка логирования
logging.basicConfig(filename="logs/bot.log", level=logging.INFO, format="%(asctime)s - %(message)s")

# Загрузка конфигурации
with open("config/config.yaml", "r") as f:
    config = yaml.safe_load(f)

TELEGRAM_TOKEN = config["telegram_token"]

# Запуск бота
def main():
    updater = Updater(TELEGRAM_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_telegram_message))
    dp.add_handler(CommandHandler("whatsapp", handle_whatsapp_message))

    updater.start_polling()
    logging.info("Bot started")
    updater.idle()

if __name__ == "__main__":
    main()
