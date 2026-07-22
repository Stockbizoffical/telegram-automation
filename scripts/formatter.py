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
    except Exception:
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


def get_growth_icon(value):

    if value is None:
        return "⚪"

    try:
        value = float(value)

        if value >= 20:
            return "🟢"

        elif value >= 0:
            return "🟡"

        else:
            return "🔴"

    except Exception:
        return "⚪"


def format_ai_analysis(company, analysis):

    if not analysis:
        return ""

    financial = analysis.get("financial_data", {})
    trend = analysis.get("trend", {})
    quality = analysis.get("quality", {})
    score = analysis.get("score", {})
    growth = analysis.get("growth", {})

    message = f"""
📊 <b>{company}</b>

━━━━━━━━━━━━━━━━━━

⭐ <b>AI Score :</b> {score.get("score","-")}/100

📈 <b>Signal :</b> {score.get("signal","-")}

📝 <b>Verdict :</b>
{score.get("verdict","-")}

━━━━━━━━━━━━━━━━━━

<b>Financial Highlights</b>

"""

    metrics = [

        ("Revenue", "revenue_growth"),
        ("PAT", "pat_growth"),
        ("EBITDA", "ebitda_growth"),
        ("EPS", "eps_growth")

    ]

    for metric, growth_key in metrics:

        value = "-"

        if metric in financial:
            value = financial[metric].get("Current", "-")

        growth_value = growth.get(growth_key)

        icon = get_growth_icon(growth_value)

        message += f"{icon} <b>{metric}</b>\n"

        message += f"{value}"

        if growth_value is not None:
            message += f" ({growth_value:.2f}%)"

        message += "\n\n"

    remarks = quality.get("remarks", [])

    if remarks:

        message += "━━━━━━━━━━━━━━━━━━\n\n"

        message += "🤖 <b>AI Analysis</b>\n\n"

        for remark in remarks:
            message += f"• {remark}\n"

        message += "\n"

    impact = trend.get("Impact Score")

    if impact is not None:

        message += f"⭐ <b>Impact Score :</b> {impact}/100\n\n"

    message += """
━━━━━━━━━━━━━━━━━━

🚀 <b>Powered by Stock Biz AI</b>
"""

    return message
