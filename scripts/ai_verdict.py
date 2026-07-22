"""
Stock Biz AI
AI Verdict Engine
"""


def generate_verdict(growth, score):
    """
    Generate AI-based financial verdict
    """

    remarks = []

    revenue = growth.get("revenue_growth")
    pat = growth.get("pat_growth")
    ebitda = growth.get("ebitda_growth")
    eps = growth.get("eps_growth")

    ai_score = score.get("score", 0)

    # ----------------------------
    # Revenue Analysis
    # ----------------------------

    if revenue is not None:

        if revenue >= 20:
            remarks.append("Revenue registered strong growth.")

        elif revenue >= 10:
            remarks.append("Revenue growth remained healthy.")

        elif revenue > 0:
            remarks.append("Revenue improved marginally.")

        else:
            remarks.append("Revenue declined during the quarter.")

    # ----------------------------
    # PAT Analysis
    # ----------------------------

    if pat is not None:

        if pat >= 25:
            remarks.append("Net profit improved significantly.")

        elif pat >= 10:
            remarks.append("Net profit registered healthy growth.")

        elif pat > 0:
            remarks.append("Net profit improved slightly.")

        else:
            remarks.append("Profit after tax declined.")

    # ----------------------------
    # EBITDA Analysis
    # ----------------------------

    if ebitda is not None:

        if ebitda >= 15:
            remarks.append("Operating performance remained strong.")

        elif ebitda > 0:
            remarks.append("Operating performance remained stable.")

        else:
            remarks.append("Operating performance weakened.")

    # ----------------------------
    # EPS Analysis
    # ----------------------------

    if eps is not None:

        if eps >= 15:
            remarks.append("EPS growth remained strong.")

        elif eps > 0:
            remarks.append("EPS improved during the quarter.")

        else:
            remarks.append("EPS declined.")

    # ----------------------------
    # Combined Analysis
    # ----------------------------

    if revenue is not None and pat is not None:

        if revenue > 0 and pat > revenue:

            remarks.append(
                "Profit growth exceeded revenue growth, indicating improving profitability."
            )

        elif revenue > pat > 0:

            remarks.append(
                "Revenue grew faster than profit, suggesting margin pressure."
            )

        elif revenue < 0 and pat > 0:

            remarks.append(
                "Profit increased despite lower revenue, indicating effective cost management."
            )

    # ----------------------------
    # Overall Verdict
    # ----------------------------

    if ai_score >= 90:

        verdict = "Excellent"

        investment = "STRONG BUY"

        risk = "LOW"

    elif ai_score >= 75:

        verdict = "Strong"

        investment = "BUY"

        risk = "LOW"

    elif ai_score >= 60:

        verdict = "Average"

        investment = "HOLD"

        risk = "MEDIUM"

    elif ai_score >= 40:

        verdict = "Weak"

        investment = "REDUCE"

        risk = "HIGH"

    else:

        verdict = "Poor"

        investment = "AVOID"

        risk = "VERY HIGH"

    return {

        "remarks": remarks,

        "verdict": verdict,

        "investment": investment,

        "risk": risk

    }
