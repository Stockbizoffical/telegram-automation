import os

from scripts.telegram import send_message
from scripts.bse import get_bse_announcements

try:
    data = get_bse_announcements()

    if data:
        message = "✅ BSE API Connected Successfully!"
    else:
        message = "❌ No data received from BSE API."

except Exception as e:
    message = f"❌ Error:\n{e}"

send_message(message)

print("Message Sent Successfully")
