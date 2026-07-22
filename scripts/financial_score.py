"""
Stock Biz AI
Financial Score Engine
"""


def calculate_financial_score(growth, quality):
    """
    Calculate AI Financial Score
    """

    score = 0

    # Revenue Growth (20 Marks)
    revenue = growth.get("revenue_growth")
    if revenue is not None:
        if revenue >= 20:
            score += 20
        elif revenue >= 10:
            score += 15
        elif revenue > 0:
            score += 10

    # PAT Growth (25 Marks)
    pat = growth.get("pat_growth")
    if pat is not None:
        if pat >= 25:
            score += 25
        elif pat >= 15:
            score += 18
        elif pat > 0:
            score += 12

    # EBITDA Growth (20 Marks)
    ebitda = growth.get("ebitda_growth")
    if ebitda is not None:
        if ebitda >= 20:
            score += 20
        elif ebitda >= 10:
            score += 15
        elif ebitda > 0:
            score += 10

    # EPS Growth (15 Marks)
    eps = growth.get("eps_growth")
    if eps is not None:
        if eps >= 20:
            score += 15
        elif eps >= 10:
            score += 10
        elif eps > 0:
            score += 5

    # Quality Score (20 Marks)
    rating = str(quality.get("rating", "")).lower()

    if rating == "excellent":
        score += 20
    elif rating == "good":
        score += 15
    elif rating == "average":
        score += 10
    elif rating == "poor":
        score += 5

    # Maximum Score = 100
    score = min(score, 100)

    # Final Verdict
    if score >= 90:
        verdict = "Excellent Quarterly Result"
        signal = "STRONG BUY"
        color = "GREEN"

    elif score >= 75:
        verdict = "Strong Quarterly Result"
        signal = "BUY"
        color = "GREEN"

    elif score >= 60:
        verdict = "Average Quarterly Result"
        signal = "HOLD"
        color = "YELLOW"

    elif score >= 40:
        verdict = "Weak Quarterly Result"
        signal = "SELL"
        color = "ORANGE"

    else:
        verdict = "Poor Quarterly Result"
        signal = "AVOID"
        color = "RED"

    return {

        "score": score,

        "verdict": verdict,

        "signal": signal,

        "color": color

    }
