import os
import requests

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHANNEL_ID = os.environ["CHANNEL_ID"]

message = """
🚀 Stock Biz Automation Started Successfully!

✅ Telegram Bot Connected
✅ GitHub Actions Working

यह पहला Test Message है।
"""

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

payload = {
    "chat_id": CHANNEL_ID,
    "text": message
}

response = requests.post(url, data=payload)

print(response.text)
