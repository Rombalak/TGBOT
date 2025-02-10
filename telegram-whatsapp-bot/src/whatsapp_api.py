import requests
import yaml
import logging

# Загрузка конфигурации
with open("config/config.yaml", "r") as f:
    config = yaml.safe_load(f)

WHATSAPP_API_URL = config["whatsapp_api_url"]
WHATSAPP_API_KEY = config["whatsapp_api_key"]

def send_whatsapp_message(phone, message):
    """Отправка сообщения в WhatsApp через бесплатное API"""
    data = {
        "phone": phone,
        "message": message,
        "key": WHATSAPP_API_KEY
    }
    response = requests.post(f"{WHATSAPP_API_URL}/send", json=data)

    if response.status_code == 200:
        logging.info(f"Sent to WhatsApp [{phone}]: {message}")
        return True
    else:
        logging.error(f"WhatsApp API error: {response.text}")
        return False
