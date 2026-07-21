from scripts.bse import get_bse_announcements
from scripts.telegram import send_message
from scripts.storage import get_last_news, save_last_news

SOURCE = "bse"

announcements = get_bse_announcements()

if not announcements:
    print("No announcements found.")
    exit()

first = announcements[0]

news_id = first.get("NEWSID", "")

last_news = get_last_news(SOURCE)

if news_id == last_news:
    print("No new announcement.")
    exit()

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
    message += f"""

📄 PDF
{pdf}
"""

message += """

━━━━━━━━━━━━━━━━━━
🚀 Stock Biz AI Automation
"""

send_message(message)

save_last_news(SOURCE, news_id)

print("Announcement sent successfully.")
