import requests
from scripts.config import BOT_TOKEN, CHANNEL_ID


def send_message(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    payload = {
        "chat_id": CHANNEL_ID,
        "text": message,
        "parse_mode": "HTML",
        "disable_web_page_preview": True
    }

    response = requests.post(url, json=payload)

    if response.status_code == 200:
        print("✅ Telegram Message Sent Successfully")
    else:
        print("❌ Telegram Error")
        print(response.text)
