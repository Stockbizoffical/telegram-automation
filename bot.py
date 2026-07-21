from scripts.bse import get_bse_announcements
from scripts.telegram import send_message
from scripts.storage import get_last_news, save_last_news
from scripts.formatter import format_bse_announcement

SOURCE = "bse"


def main():
    announcements = get_bse_announcements()

    if not announcements:
        print("❌ No announcements found.")
        return

    first = announcements[0]

    news_id = first.get("NEWSID", "")

    last_news = get_last_news(SOURCE)

    if news_id == last_news:
        print("✅ No new announcement.")
        return

    save_last_news(SOURCE, news_id)

    message = format_bse_announcement(first)

    send_message(message)

    print("✅ Announcement Sent Successfully")


if __name__ == "__main__":
    main()
