"""
Stock Biz AI
Quality Analyzer
"""


def analyze_quality(trend):

    score = trend.get("Impact Score", 50)

    revenue = trend.get("Revenue Growth")
    pat = trend.get("PAT Growth")
    eps = trend.get("EPS Growth")

    remarks = []

    # Revenue Analysis
    if revenue is not None:

        if revenue >= 15:
            remarks.append("📈 Strong Revenue Growth")

        elif revenue >= 5:
            remarks.append("🟡 Moderate Revenue Growth")

        else:
            remarks.append("🔴 Weak Revenue Growth")

    # PAT Analysis
    if pat is not None:

        if pat >= 20:
            remarks.append("💰 Strong Profit Growth")

        elif pat >= 10:
            remarks.append("🟡 Moderate Profit Growth")

        else:
            remarks.append("🔴 Weak Profit Growth")

    # EPS Analysis
    if eps is not None:

        if eps >= 15:
            remarks.append("📊 EPS Improving")

        elif eps >= 5:
            remarks.append("🟡 EPS Stable")

        else:
            remarks.append("🔴 EPS Weak")

    # Final Verdict
    if score >= 90:
        verdict = "🚀 Excellent Quarterly Performance"

    elif score >= 75:
        verdict = "🟢 Strong Quarterly Performance"

    elif score >= 60:
        verdict = "🟡 Average Quarterly Performance"

    else:
        verdict = "🔴 Weak Quarterly Performance"

    return {
        "remarks": remarks,
        "verdict": verdict,
        "confidence": score
    }
