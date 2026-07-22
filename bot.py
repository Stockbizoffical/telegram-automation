from scripts.bse import get_bse_announcements
from scripts.telegram import send_message
from scripts.storage import save_news
from scripts.formatter import (
    format_bse_announcement,
    format_ai_analysis,
)
from scripts.engine import get_valid_announcements
from scripts.logger import log
from scripts.pipeline import analyze_pdf
from scripts.result_detector import is_financial_result
from scripts.pdf_url_builder import build_pdf_url

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
    company = announcement.get("SLONGNAME", "Unknown Company")

    try:

        # Default Telegram Message
        message = format_bse_announcement(announcement)

        # Attachment File Name
        attachment_name = announcement.get("ATTACHMENTNAME", "")

        # Build Complete PDF URL
        pdf_url = build_pdf_url(attachment_name)

        # AI Analysis only for Financial Results
        if pdf_url and is_financial_result(announcement):

            log(f"Financial Result Detected : {company}")
            log(f"PDF URL : {pdf_url}")

            analysis = analyze_pdf(pdf_url)

            if analysis:

                message = format_ai_analysis(company, analysis)

                log(f"AI Analysis Completed : {company}")

            else:

                log(f"AI Analysis Failed : {company}")

        else:

            log(f"Normal Announcement : {company}")

        # Send Telegram Message
        send_message(message)

        # Save Duplicate News
        save_news(SOURCE, news_id)

        print(f"✅ Sent : {company}")
        log(f"Sent : {company}")

    except Exception as e:

        print(f"❌ Error : {e}")
        log(f"Telegram Error : {e}")

print("🎉 Bot Finished Successfully")
log("Bot Finished")
