"""
Stock Biz AI
Financial Analyzer Module
"""

from typing import Optional


def calculate_growth(current, previous) -> Optional[float]:
    """
    Calculate Growth Percentage
    """

    try:
        current = float(str(current).replace(",", "").strip())
        previous = float(str(previous).replace(",", "").strip())

        if previous == 0:
            return None

        growth = ((current - previous) / previous) * 100

        return round(growth, 2)

    except Exception as e:
        print(f"Growth Calculation Error: {e}")
        return None


def get_rating(growth: Optional[float]) -> str:
    """
    Return Rating Based on Growth %
    """

    if growth is None:
        return "⚪ Unknown"

    if growth >= 30:
        return "🚀 Outstanding"

    if growth >= 20:
        return "🟢 Excellent"

    if growth >= 10:
        return "🟢 Strong"

    if growth >= 5:
        return "🟡 Positive"

    if growth >= 0:
        return "🟠 Stable"

    if growth >= -10:
        return "🔴 Weak"

    return "⚫ Poor"


def calculate_score(result: dict) -> int:
    """
    AI Impact Score
    """

    score = 50

    revenue = result.get("Revenue Growth")
    pat = result.get("PAT Growth")
    eps = result.get("EPS Growth")

    # Revenue

    if revenue is not None:

        if revenue >= 30:
            score += 20

        elif revenue >= 20:
            score += 15

        elif revenue >= 10:
            score += 10

        elif revenue >= 5:
            score += 5

    # PAT

    if pat is not None:

        if pat >= 30:
            score += 25

        elif pat >= 20:
            score += 20

        elif pat >= 10:
            score += 12

        elif pat >= 5:
            score += 6

    # EPS

    if eps is not None:

        if eps >= 20:
            score += 15

        elif eps >= 10:
            score += 10

        elif eps >= 5:
            score += 5

    return min(score, 100)
