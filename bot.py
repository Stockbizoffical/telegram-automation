from scripts.bse import get_bse_announcements
from scripts.telegram import send_message

announcements = get_bse_announcements()

if not announcements:
    send_message("❌ No BSE announcements found.")
    exit()

first = announcements[0]

company = first.get("SLONGNAME", "N/A")
subject = first.get("NEWSSUB", "N/A")
date = first.get("NEWS_DT", "N/A")
pdf = first.get("NSURL", "")

message = f"""📢 BSE Corporate Announcement

🏢 Company
{company}

📌 Subject
{subject}

📅 Date
{date}
"""

if pdf:
    message += f"\n📄 PDF\n{pdf}\n"

message += """

━━━━━━━━━━━━━━━━━━
🚀 Stock Biz AI Automation
"""

send_message(message)
