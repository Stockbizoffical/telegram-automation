"""
Stock Biz AI
Trend Analyzer
"""

from scripts.financial_analyzer import calculate_growth
from scripts.financial_analyzer import get_rating
from scripts.financial_analyzer import calculate_score


def analyze_trends(financial_data):

    result = {}

    for metric in ["Revenue", "PAT", "EBITDA", "EPS"]:

        if metric not in financial_data:
            continue

        current = financial_data[metric].get("Current")
        previous = financial_data[metric].get("Previous")

        growth = calculate_growth(current, previous)

        result[f"{metric} Growth"] = growth
        result[f"{metric} Rating"] = get_rating(growth)

    result["Impact Score"] = calculate_score(result)

    score = result["Impact Score"]

    if score >= 90:
        result["Verdict"] = "🚀 Very Bullish"

    elif score >= 75:
        result["Verdict"] = "🟢 Bullish"

    elif score >= 60:
        result["Verdict"] = "🟡 Neutral"

    else:
        result["Verdict"] = "🔴 Weak"

    return result
