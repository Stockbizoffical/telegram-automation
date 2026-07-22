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
def format_ai_analysis(company, analysis):

    if not analysis:
        return ""

    trend = analysis.get("trend", {})
    quality = analysis.get("quality", {})
    financial = analysis.get("financial_data", {})

    message = f"📊 <b>{company}</b>\n\n"

    message += "📈 <b>Financial Snapshot</b>\n\n"

    for metric in ["Revenue", "PAT", "EBITDA", "EPS"]:

        if metric in financial:

            current = financial[metric].get("Current", "-")
            growth = trend.get(f"{metric} Growth")

            message += f"<b>{metric}</b>\n"

            message += f"{current}"

            if growth is not None:
                message += f" ({growth}%)"

            message += "\n\n"

    message += "━━━━━━━━━━━━━━\n\n"

    message += "🤖 <b>AI Analysis</b>\n\n"

    remarks = quality.get("remarks", [])

    for remark in remarks:
        message += f"{remark}\n"

    message += "\n"

    message += f"⭐ <b>Impact Score</b> : {trend.get('Impact Score', '-')}/100\n\n"

    message += f"🚀 <b>Verdict</b>\n"

    message += quality.get("verdict", "-")

    return message
