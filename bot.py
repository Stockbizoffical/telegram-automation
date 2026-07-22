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

# ---------------------------------
# Fetch Announcements
# ---------------------------------

announcements = get_bse_announcements()

if not announcements:
    print("❌ No announcements found.")
    log("No announcements found")
    exit()

# ---------------------------------
# Filter High Priority News
# ---------------------------------

announcements = get_valid_announcements(
    announcements,
    SOURCE
)

if not announcements:
    print("ℹ️ No High Priority Announcements.")
    log("No High Priority Announcements")
    exit()

# ---------------------------------
# Process News
# ---------------------------------

for announcement in announcements:

    news_id = announcement.get("NEWSID", "")
    company = announcement.get("SLONGNAME", "Unknown Company")

    log(f"Processing : {company}")

    try:

        # Default Message
        message = format_bse_announcement(
            announcement
        )

        attachment = announcement.get(
            "ATTACHMENTNAME",
            ""
        )

        pdf_url = build_pdf_url(
            attachment
        )

        # ------------------------------
        # AI Analysis
        # ------------------------------

        if pdf_url and is_financial_result(announcement):

            log("Financial Result Detected")

            log(f"PDF : {pdf_url}")

            analysis = analyze_pdf(pdf_url)

            if analysis:

                ai_message = format_ai_analysis(
                    company,
                    analysis
                )

                if ai_message:
                    message = ai_message
                    log("AI Formatter Success")

                else:
                    log("AI Formatter Returned Empty")

            else:

                log("AI Pipeline Failed")

        else:

            log("Normal Corporate Announcement")

        # ------------------------------
        # Send Telegram
        # ------------------------------

        if message:

            send_message(message)

            save_news(
                SOURCE,
                news_id
            )

            print(f"✅ Sent : {company}")

            log(f"Sent : {company}")

        else:

            log("Empty Message Skipped")

    except Exception as e:

        print(f"❌ Error : {company}")

        print(e)

        log(f"{company} : {e}")

print("🎉 Bot Finished Successfully")

log("Bot Finished")
