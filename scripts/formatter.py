from datetime import datetime
from html import escape


def safe(value, default="-"):
    """Return safe string value."""
    if value is None:
        return default

    if isinstance(value, str):
        value = value.strip()
        if not value:
            return default

    return str(value)


def format_number(value):
    """Format numbers nicely."""

    if value in (None, "-", ""):
        return "-"

    try:
        num = float(str(value).replace(",", ""))

        if abs(num) >= 10000000:
            return f"{num/10000000:.2f} Cr"

        elif abs(num) >= 100000:
            return f"{num/100000:.2f} L"

        elif num.is_integer():
            return f"{int(num):,}"

        return f"{num:,.2f}"

    except Exception:
        return str(value)


def get_growth_icon(value):

    if value is None:
        return "⚪"

    try:

        value = float(value)

        if value >= 20:
            return "🟢"

        elif value >= 10:
            return "🟩"

        elif value >= 0:
            return "🟡"

        else:
            return "🔴"

    except Exception:
        return "⚪"


def get_signal_icon(signal):

    signal = str(signal).upper()

    mapping = {
        "BUY": "🟢",
        "STRONG BUY": "🚀",
        "HOLD": "🟡",
        "SELL": "🔴",
        "STRONG SELL": "⛔"
    }

    return mapping.get(signal, "⚪")


def get_star(score):

    try:

        score = float(score)

        if score >= 90:
            return "★★★★★"

        elif score >= 75:
            return "★★★★☆"

        elif score >= 60:
            return "★★★☆☆"

        elif score >= 40:
            return "★★☆☆☆"

        return "★☆☆☆☆"

    except Exception:
    return "-"


def format_bse_announcement(data):
    """
    Format BSE Corporate Announcement
    """

    company = escape(safe(data.get("SLONGNAME", "N/A")))
    subject = escape(safe(data.get("NEWSSUB", "N/A")))
    pdf = safe(data.get("NSURL", ""))
    raw_date = data.get("NEWS_DT", "")
    category = str(data.get("CATEGORY", "OTHER")).upper()

    try:
        dt = datetime.fromisoformat(raw_date)
        date = dt.strftime("%d %b %Y | %I:%M %p")
    except Exception:
        date = safe(raw_date)

    category_icon = {
        "RESULT": "📊",
        "FINANCIAL RESULTS": "📊",
        "DIVIDEND": "💰",
        "BONUS": "🎁",
        "SPLIT": "✂️",
        "BOARD": "📅",
        "BOARD MEETING": "📅",
        "BULK": "🤝",
        "BLOCK": "🏦",
        "AGM": "👥",
        "EGM": "👥",
        "PREFERENTIAL ISSUE": "🪙",
        "RIGHTS": "📜",
        "MERGER": "🔄",
        "ACQUISITION": "🤝",
        "OTHER": "📢",
    }

    icon = category_icon.get(category, "📢")

    message = f"""
🚀 <b>Stock Biz AI</b>

━━━━━━━━━━━━━━━━━━

{icon} <b>BSE Corporate Announcement</b>

🏢 <b>Company</b>

{company}

📌 <b>Category</b>

{escape(category)}

📄 <b>Subject</b>

{subject}

📅 <b>Announcement Time</b>

{date}
"""

    if pdf:

        message += f"""

━━━━━━━━━━━━━━━━━━

📄 <b>Official PDF</b>

{pdf}
"""

    message += """

━━━━━━━━━━━━━━━━━━

⚡ <b>Source :</b> BSE India

🤖 <b>Status :</b> PDF Received Successfully

🚀 <b>Powered by Stock Biz AI</b>
"""

    return message.strip()


def format_ai_analysis(company, analysis):
    if not analysis:
        return ""

    ai = analysis.get("ai_engine", {})

    financial = analysis.get("financials") or analysis.get("financial_data", {})
    financial = financial if isinstance(financial, dict) else {}
    growth = analysis.get("growth", {})
    trend = analysis.get("trend", {})
    quality = analysis.get("quality", {})
    score = analysis.get("score", {})

    ai_score = ai.get("score") or score.get("score", 0)
    signal = ai.get("signal") or score.get("signal", "HOLD")
    verdict = ai.get("verdict", score.get("verdict", "-"))
    investment = ai.get("investment_view", "-")
    risk = ai.get("risk", "-")

    signal_icon = get_signal_icon(signal)

    message = f"""
🚀 <b>Stock Biz AI Financial Report</b>

━━━━━━━━━━━━━━━━━━

🏢 <b>Company</b>

{escape(company)}

━━━━━━━━━━━━━━━━━━

⭐ <b>AI Score</b>

{ai_score}/100

{signal_icon} <b>Signal</b>

{signal}

━━━━━━━━━━━━━━━━━━

📊 <b>Financial Highlights</b>

"""

    metrics = [

        ("Revenue", "revenue_growth", "📈"),
        ("PAT", "pat_growth", "💰"),
        ("EBITDA", "ebitda_growth", "⚙️"),
        ("EPS", "eps_growth", "💵"),

    ]

    for metric, growth_key, emoji in metrics:

        current = "-"

        if metric in financial:

            current = financial[metric].get("Current", "-")

        current = format_number(current)

        growth_value = growth.get(growth_key)

        icon = get_growth_icon(growth_value)

        message += f"{emoji} <b>{metric}</b>\n"

        message += f"Current : {current}\n"

        if growth_value is not None:

            message += f"{icon} Growth : {growth_value:.2f}%\n"

        else:

            message += "Growth : -\n"

        message += "\n"

    message += "━━━━━━━━━━━━━━━━━━\n\n"

    message += f"🎯 <b>Verdict</b>\n\n{verdict}\n\n"

    message += f"💡 <b>Investment View</b>\n\n{investment}\n\n"

    message += f"⚠️ <b>Risk Level</b>\n\n{risk}\n\n"

    summary = ai.get("summary", [])

    if isinstance(summary, str):
        summary = [summary]

    if summary:

        message += "━━━━━━━━━━━━━━━━━━\n\n"

        message += "🧠 <b>AI Insights</b>\n\n"

        for item in summary:

            if item:
                message += f"• {escape(str(item))}\n"

        message += "\n"

    remarks = quality.get("remarks", [])

    if remarks:

        message += "━━━━━━━━━━━━━━━━━━\n\n"

        message += "📋 <b>Quality Analysis</b>\n\n"

        for remark in remarks:

            message += f"• {escape(str(remark))}\n"

        message += "\n"

    impact = trend.get("Impact Score")

    if impact is not None:

        message += "━━━━━━━━━━━━━━━━━━\n\n"

        message += f"⭐ <b>Impact Score</b> : {impact}/100\n\n"

    message += "━━━━━━━━━━━━━━━━━━\n\n"

    message += f"📊 <b>Financial Health</b>\n\n{get_star(ai_score)}\n\n"

    message += "━━━━━━━━━━━━━━━━━━\n\n"

    message += (
        "🤖 <b>Generated by Stock Biz AI</b>\n"
        "⚡ <b>Automated Financial Analysis</b>\n"
        "📈 <b>Source :</b> BSE India\n\n"
        "🚀 <b>Powered by Stock Biz AI</b>"
    )

    return message
