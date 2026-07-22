from scripts.bse import get_bse_announcements
from scripts.telegram import send_message
from scripts.storage import get_last_news, save_last_news
from scripts.formatter import format_bse_announcement
from scripts.engine import get_valid_announcements

SOURCE = "bse"

print("🚀 Stock Biz AI Bot Started")

announcements = get_bse_announcements()

if not announcements:
    print("❌ No announcements found.")
    exit()

# केवल Valid Categories
announcements = get_valid_announcements(announcements)

if not announcements:
    print("ℹ️ No High Priority Announcements.")
    exit()

last_news = get_last_news(SOURCE)

for announcement in announcements:

    news_id = announcement.get("NEWSID", "")

    if news_id == last_news:
        print(f"⏩ Skip Duplicate : {news_id}")
        continue

    message = format_bse_announcement(announcement)

    send_message(message)

    save_last_news(SOURCE, news_id)

    print(f"✅ Sent : {announcement.get('SLONGNAME','')}")

print("🎉 Bot Finished Successfully")
