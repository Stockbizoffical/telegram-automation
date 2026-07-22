from scripts.bse import get_bse_announcements
from scripts.telegram import send_message
from scripts.storage import save_news
from scripts.formatter import (
    format_bse_announcement,
    format_ai_analysis
)
from scripts.engine import get_valid_announcements
from scripts.logger import log
from scripts.pipeline import analyze_pdf

SOURCE = "bse"

print("🚀 Stock Biz AI Bot Started")
log("Bot Started")

announcements = get_bse_announcements()

if not announcements:
    print("❌ No announcements found.")
    log("No announcements found")
    exit()

announcements = get_valid_announcements(announcements, SOURCE)

if not announcements:
    print("ℹ️ No High Priority Announcements.")
    log("No High Priority Announcements")
    exit()

for announcement in announcements:

    news_id = announcement.get("NEWSID", "")
    company = announcement.get("SLONGNAME", "")

    try:

        # PDF Link
        pdf_url = announcement.get("ATTACHMENTNAME", "")

        if pdf_url:

            analysis = analyze_pdf(pdf_url)

            if analysis:

                message = format_ai_analysis(company, analysis)

            else:

                message = format_bse_announcement(announcement)

        else:

            message = format_bse_announcement(announcement)

        send_message(message)

        save_news(SOURCE, news_id)

        print(f"✅ Sent : {company}")

        log(f"Sent : {company}")

    except Exception as e:

        print(e)

        log(f"Telegram Error : {e}")

print("🎉 Bot Finished Successfully")
log("Bot Finished")
