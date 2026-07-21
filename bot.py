import os
from scripts.telegram import send_message

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHANNEL_ID = os.environ["CHANNEL_ID"]

message = """
🚀 Stock Biz AI Automation

✅ Professional Project Structure Ready
✅ Telegram Module Connected

अब अगला Step:
📊 BSE + NSE Automation
🤖 AI Summary
"""

result = send_message(BOT_TOKEN, CHANNEL_ID, message)

print(result)
