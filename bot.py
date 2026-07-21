import os

from scripts.telegram import send_message
from scripts.bse import get_bse_announcements

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHANNEL_ID = os.environ["CHANNEL_ID"]

try:
    data = get_bse_announcements()

    if data:
        message = "✅ BSE API Connected Successfully"
    else:
        message = "❌ No data received from BSE"

except Exception as e:
    message = f"❌ Error:\n{e}"

result = send_message(
    BOT_TOKEN,
    CHANNEL_ID,
    message
)

print(result)
