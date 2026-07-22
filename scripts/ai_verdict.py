"""
Stock Biz AI
AI Verdict Engine
"""


def generate_verdict(growth, score):
    """
    Generate AI-based Financial Verdict
    """

    remarks = []
    strengths = []
    weaknesses = []

    revenue = growth.get("revenue_growth")
    pat = growth.get("pat_growth")
    ebitda = growth.get("ebitda_growth")
    eps = growth.get("eps_growth")

    ai_score = score.get("score", 0)

    # ----------------------------
    # Revenue
    # ----------------------------

    if revenue is not None:

        if revenue >= 20:
            remarks.append("Revenue registered strong growth.")
            strengths.append("Strong Revenue Growth")

        elif revenue >= 10:
            remarks.append("Revenue growth remained healthy.")
            strengths.append("Healthy Revenue Growth")

        elif revenue >= 0:
            remarks.append("Revenue improved marginally.")

        else:
            remarks.append("Revenue declined during the quarter.")
            weaknesses.append("Revenue Decline")

    # ----------------------------
    # PAT
    # ----------------------------

    if pat is not None:

        if pat >= 25:
            remarks.append("Net profit improved significantly.")
            strengths.append("Strong Profit Growth")

        elif pat >= 10:
            remarks.append("Net profit registered healthy growth.")
            strengths.append("Healthy Profit Growth")

        elif pat >= 0:
            remarks.append("Net profit improved slightly.")

        else:
            remarks.append("Profit after tax declined.")
            weaknesses.append("PAT Decline")

    # ----------------------------
    # EBITDA
    # ----------------------------

    if ebitda is not None:

        if ebitda >= 15:
            remarks.append("Operating performance remained strong.")
            strengths.append("Healthy EBITDA")

        elif ebitda >= 0:
            remarks.append("Operating performance remained stable.")

        else:
            remarks.append("Operating performance weakened.")
            weaknesses.append("Weak EBITDA")

    # ----------------------------
    # EPS
    # ----------------------------

    if eps is not None:

        if eps >= 15:
            remarks.append("EPS growth remained strong.")
            strengths.append("Strong EPS Growth")

        elif eps >= 0:
            remarks.append("EPS improved during the quarter.")

        else:
            remarks.append("EPS declined.")
            weaknesses.append("EPS Decline")

    # ----------------------------
    # Combined Analysis
    # ----------------------------

    if revenue is not None and pat is not None:

        if revenue > 0 and pat > revenue:

            remarks.append(
                "Profit growth exceeded revenue growth, indicating improving profitability."
            )

            strengths.append("Profitability Improved")

        elif revenue > pat > 0:

            remarks.append(
                "Revenue grew faster than profit, indicating margin pressure."
            )

            weaknesses.append("Margin Pressure")

        elif revenue < 0 and pat > 0:

            remarks.append(
                "Profit increased despite lower revenue due to cost control."
            )

            strengths.append("Good Cost Management")

    # ----------------------------
    # AI Verdict
    # ----------------------------

    if ai_score >= 90:

        verdict = "Excellent Quarterly Performance"
        signal = "STRONG BUY"
        investment = "Positive"
        risk = "Low"

    elif ai_score >= 75:

        verdict = "Strong Quarterly Performance"
        signal = "BUY"
        investment = "Positive"
        risk = "Low"

    elif ai_score >= 60:

        verdict = "Average Quarterly Performance"
        signal = "HOLD"
        investment = "Neutral"
        risk = "Medium"

    elif ai_score >= 40:

        verdict = "Weak Quarterly Performance"
        signal = "SELL"
        investment = "Negative"
        risk = "High"

    else:

        verdict = "Poor Quarterly Performance"
        signal = "STRONG SELL"
        investment = "Avoid"
        risk = "Very High"

    return {

        "remarks": remarks,

        "strengths": strengths,

        "weaknesses": weaknesses,

        "verdict": verdict,

        "signal": signal,

        "investment": investment,

        "risk": risk

    }
