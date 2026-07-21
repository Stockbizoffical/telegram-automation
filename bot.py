from scripts.bse import get_bse_announcements
from scripts.telegram import send_message
from scripts.storage import get_last_news, save_last_news
from scripts.formatter import format_bse_announcement
from scripts.filters import get_category

SOURCE = "bse"

announcements = get_bse_announcements()

if not announcements:
    print("❌ No announcements found.")
    exit()

first = announcements[0]

news_id = first.get("NEWSID", "")
subject = first.get("NEWSSUB", "")

# Duplicate Filter
last_news = get_last_news(SOURCE)

if news_id == last_news:
    print("✅ No new announcement.")
    exit()

save_last_news(SOURCE, news_id)

# Category Detection
category = get_category(subject)

print(f"Category : {category}")

# अभी सभी Category Telegram पर भेजेंगे
# अगले Step में केवल Selected Category भेजेंगे

message = format_bse_announcement(first)

send_message(message)
