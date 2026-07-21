from scripts.bse import get_bse_announcements
from scripts.telegram import send_message
from scripts.storage import get_last_news, save_last_news

announcements = get_bse_announcements()

if not announcements:
    send_message("❌ No BSE announcements found.")
    exit()

first = announcements[0]

# Unique News ID
news_id = first.get("NEWSID", "")

# Check duplicate
last_news = get_last_news()

if news_id == last_news:
    print("No new announcement.")
    exit()

# Save latest news id
save_last_news(news_id)

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
