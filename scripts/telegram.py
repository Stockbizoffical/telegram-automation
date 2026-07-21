import requests
from scripts.config import BOT_TOKEN, CHANNEL_ID

def send_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    data = {
        "chat_id": CHANNEL_ID,
        "text": text
    }

    requests.post(url, data=data)
