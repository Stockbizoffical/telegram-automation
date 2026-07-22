from scripts.bse import get_bse_announcements
from scripts.telegram import send_message
from scripts.storage import save_news
from scripts.formatter import (
    format_bse_announcement,
    format_ai_analysis,
)
from scripts.engine import get_valid_announcements
from scripts.logger import (
    info,
    warning,
    error,
    success,
    ai,
    result,
)
from scripts.pipeline import analyze_pdf
from scripts.result_detector import is_financial_result
from scripts.pdf_url_builder import build_pdf_url

SOURCE = "bse"

print("🚀 Stock Biz AI Bot Started")
info("Bot Started")

# ---------------------------------
# Fetch Announcements
# ---------------------------------

announcements = get_bse_announcements()

if not announcements:
    print("❌ No announcements found.")
    warning("No announcements found")
    exit()

# ---------------------------------
# Filter High Priority Announcements
# ---------------------------------

announcements = get_valid_announcements(
    announcements,
    SOURCE
)

if not announcements:
    print("ℹ️ No High Priority Announcements.")
    info("No High Priority Announcements")
    exit()

# ---------------------------------
# Process Announcements
# ---------------------------------

for announcement in announcements:

    news_id = announcement.get("NEWSID", "")
    company = announcement.get("SLONGNAME", "Unknown Company")

    info(f"Processing : {company}")

    try:

        # Default Telegram Message
        message = format_bse_announcement(announcement)

        # Build PDF URL
        attachment = announcement.get("ATTACHMENTNAME", "")
        pdf_url = build_pdf_url(attachment)

        # ---------------------------------
        # AI Financial Analysis
        # ---------------------------------

        if pdf_url and is_financial_result(announcement):

            result(f"Financial Result Detected : {company}")

            info(f"PDF URL : {pdf_url}")

            analysis = analyze_pdf(pdf_url)

            if not isinstance(analysis, dict):
                analysis = {}

            if analysis:

                ai_message = format_ai_analysis(
                    company,
                    analysis
                )

                if ai_message and ai_message.strip():

                    message = ai_message

                    ai(
                        f"AI Analysis Completed : {company}"
                    )

                else:

                    warning(
                        f"AI Formatter Returned Empty : {company}"
                    )

            else:

                warning(
                    f"AI Pipeline Failed : {company}"
                )

        else:

            info(
                f"Normal Corporate Announcement : {company}"
            )

        # ---------------------------------
        # Send Telegram Message
        # ---------------------------------

        if not message:

            warning(
                f"Empty Message Skipped : {company}"
            )

            continue

        if send_message(message):

            save_news(
                SOURCE,
                news_id
            )

            print(f"✅ Sent : {company}")

            success(
                f"Telegram Sent : {company}"
            )

        else:

            warning(
                f"Telegram Send Failed : {company}"
            )

    except Exception as e:

        print(f"❌ Error : {company}")
        print(e)

        error(f"{company} : {e}")

print("🎉 Bot Finished Successfully")

success("Bot Finished")
