from scripts.bse import get_bse_announcements
from scripts.telegram import send_message
from scripts.storage import get_last_news, save_last_news
from scripts.formatter import format_bse_announcement
from scripts.filters import get_category

SOURCE = "bse"

# केवल ये Categories Telegram पर जाएंगी
ALLOWED_CATEGORIES = [
    "RESULT",
    "DIVIDEND",
    "BONUS",
    "SPLIT",
    "BOARD",
    "BULK",
]

announcements = get_bse_announcements()

if not announcements:
    print("❌ No announcements found.")
    exit()

for announcement in announcements:

    news_id = announcement.get("NEWSID", "")
    subject = announcement.get("NEWSSUB", "")

    # Duplicate Filter
    last_news = get_last_news(SOURCE)

    if news_id == last_news:
        continue

    # Save Latest News ID
    save_last_news(SOURCE, news_id)

    # Detect Category
    category = get_category(subject)

    print(f"Category : {category}")

    # केवल Selected Categories भेजें
    if category not in ALLOWED_CATEGORIES:
        continue

    # Telegram Message
    message = format_bse_announcement(announcement)

    send_message(message)

print("✅ Bot Finished Successfully")
