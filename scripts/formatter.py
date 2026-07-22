from datetime import datetime
from html import escape


def safe(value, default="-"):
    """
    Return safe string value.
    """

    if value is None:
        return default

    if isinstance(value, str):
        value = value.strip()

        if not value:
            return default

    return str(value)


def format_number(value):
    """
    Format Financial Numbers
    """

    if value in (None, "-", ""):
        return "-"

    try:

        num = float(str(value).replace(",", ""))

        if abs(num) >= 10000000:
            return f"₹{num / 10000000:.2f} Cr"

        elif abs(num) >= 100000:
            return f"₹{num / 100000:.2f} L"

        elif abs(num) >= 1000:
            return f"₹{num:,.0f}"

        elif num.is_integer():
            return f"₹{int(num)}"

        return f"₹{num:,.2f}"

    except Exception:

        return str(value)


def get_growth_icon(value):
    """
    Growth Icon
    """

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

        return "🔴"

    except Exception:

        return "⚪"


def get_signal_icon(signal):
    """
    Signal Icon
    """

    signal = str(signal).upper()

    mapping = {

        "STRONG BUY": "🚀",
        "BUY": "🟢",
        "HOLD": "🟡",
        "SELL": "🔴",
        "AVOID": "⛔",
        "STRONG SELL": "⛔",

    }

    return mapping.get(signal, "⚪")


def get_star(score):
    """
    Rating Stars
    """

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
        "RIGHTS": "📜",
        "MERGER": "🔄",
        "ACQUISITION": "🤝",
        "PREFERENTIAL ISSUE": "🪙",
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
    """
    Format AI Financial Analysis
    """

    if not analysis:
        return ""

    ai = analysis.get("ai_engine", {})
    growth = analysis.get("growth", {})
    trend = analysis.get("trend", {})
    quality = analysis.get("quality", {})
    score = analysis.get("score", {})

    ai_score = ai.get("score", score.get("score", 0))
    signal = ai.get("signal", score.get("signal", "HOLD"))
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

{get_star(ai_score)}

<b>{ai_score}/100</b>

{signal_icon} <b>Signal</b>

{escape(str(signal))}

━━━━━━━━━━━━━━━━━━

📊 <b>Financial Highlights</b>

"""

    metrics = [

        ("Revenue", "revenue", "📈"),
        ("PAT", "pat", "💰"),
        ("EBITDA", "ebitda", "⚙️"),
        ("EPS", "eps", "💵"),

    ]

    for title, key, emoji in metrics:

        current = growth.get(f"{key}_current")
        previous = growth.get(f"{key}_previous")
        growth_value = growth.get(f"{key}_growth")

        current = format_number(current)
        previous = format_number(previous)

        icon = get_growth_icon(growth_value)

        if growth_value is None:

            growth_text = "-"

        elif growth_value >= 0:

            growth_text = f"+{growth_value:.2f}%"

        else:

            growth_text = f"{growth_value:.2f}%"

        message += (
            f"{emoji} <b>{title}</b>\n"
            f"Current  : {current}\n"
            f"Previous : {previous}\n"
            f"{icon} Growth : {growth_text}\n\n"
        )

    message += "━━━━━━━━━━━━━━━━━━\n\n"

    message += f"🎯 <b>Verdict</b>\n\n"

    message += f"{escape(str(verdict))}\n\n"

    message += f"💡 <b>Investment View</b>\n\n"

    message += f"{escape(str(investment))}\n\n"

    message += f"⚠️ <b>Risk Level</b>\n\n"

    message += f"{escape(str(risk))}\n\n"

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

            if remark:
                message += f"• {escape(str(remark))}\n"

        message += "\n"

    impact = trend.get("Impact Score")

    if impact is not None:

        message += "━━━━━━━━━━━━━━━━━━\n\n"

        message += f"⭐ <b>Impact Score</b>\n\n"

        message += f"{impact}/100\n\n"

    message += "━━━━━━━━━━━━━━━━━━\n\n"

    message += "📊 <b>Financial Health</b>\n\n"

    message += f"{get_star(ai_score)}\n\n"

    message += "━━━━━━━━━━━━━━━━━━\n\n"

    message += """⚠️ <b>Disclaimer</b>

This report is generated automatically using AI.

It is intended only for educational and informational purposes.

Please consult your financial advisor and do your own research before making any investment decision.

━━━━━━━━━━━━━━━━━━

🤖 <b>Generated by Stock Biz AI</b>

⚡ <b>Automated Financial Result Analysis</b>

📈 <b>Source :</b> BSE India

🌐 <b>www.stockbiz.in</b>

🚀 <b>Powered by Stock Biz AI</b>
"""

    return message
