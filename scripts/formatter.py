from datetime import datetime


def format_bse_announcement(data):
    company = data.get("SLONGNAME", "N/A")
    subject = data.get("NEWSSUB", "N/A")
    pdf = data.get("NSURL", "")
    raw_date = data.get("NEWS_DT", "")
    category = data.get("CATEGORY", "OTHER")

    try:
        dt = datetime.fromisoformat(raw_date)
        date = dt.strftime("%d %b %Y | %I:%M %p")
    except:
        date = raw_date

    category_icon = {
        "RESULT": "📊",
        "DIVIDEND": "💰",
        "BONUS": "🎁",
        "SPLIT": "✂️",
        "BOARD": "📅",
        "BULK": "🤝",
        "OTHER": "📢",
    }

    icon = category_icon.get(category, "📢")

    message = f"""
{icon} <b>BSE Corporate Announcement</b>

🏢 <b>Company</b>
{company}

📌 <b>Category</b>
{category}

📄 <b>Subject</b>
{subject}

📅 <b>Date</b>
{date}
"""

    if pdf:
        message += f"""

🔗 <b>PDF Link</b>

{pdf}
"""

    message += """

━━━━━━━━━━━━━━━━━━
🚀 <b>Stock Biz AI Automation</b>
"""

    return message
