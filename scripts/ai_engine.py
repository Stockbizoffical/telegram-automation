"""
Stock Biz AI
Master AI Engine
"""

from scripts.ai_verdict import generate_verdict


def build_ai_engine(
    metrics,
    financials,
    growth,
    trend,
    quality,
    score,
):
    """
    Master AI Engine
    """

    verdict = generate_verdict(
        growth,
        score
    )

    executive_summary = build_summary(
        growth,
        verdict
    )

    confidence = calculate_confidence(
        financials,
        growth
    )

    return {

        "score": score.get("score", 0),

        "confidence": confidence,

        "signal": verdict.get(
    "signal",
    score.get("signal", "HOLD")
),

        "verdict": verdict.get("verdict", "Neutral"),

        "investment_view": verdict.get(
            "investment",
            "Neutral"
        ),

        "risk": verdict.get(
            "risk",
            "Medium"
        ),

        "summary": executive_summary,

        "strengths": verdict.get(
            "strengths",
            []
        ),

        "weaknesses": verdict.get(
            "weaknesses",
            []
        )

    }


def calculate_confidence(
    financials,
    growth
):
    """
    AI Confidence Score
    """

    confidence = 60

    if financials.get("Revenue"):
        confidence += 10

    if financials.get("PAT"):
        confidence += 10

    if financials.get("EBITDA"):
        confidence += 10

    if financials.get("EPS"):
        confidence += 10

    if growth.get("revenue_growth") is not None:
        confidence += 5

    if growth.get("pat_growth") is not None:
        confidence += 5

    if growth.get("ebitda_growth") is not None:
        confidence += 5

    if growth.get("eps_growth") is not None:
        confidence += 5

    return min(confidence, 100)


def build_summary(
    growth,
    verdict
):
    """
    Executive Summary
    """

    lines = []

    revenue = growth.get("revenue_growth")
    pat = growth.get("pat_growth")
    ebitda = growth.get("ebitda_growth")
    eps = growth.get("eps_growth")

    # Revenue
    if revenue is not None:

        if revenue >= 20:
            lines.append(
                "Revenue growth remained very strong."
            )

        elif revenue >= 10:
            lines.append(
                "Revenue growth remained healthy."
            )

        elif revenue >= 0:
            lines.append(
                "Revenue reported moderate growth."
            )

        else:
            lines.append(
                "Revenue declined."
            )

    # PAT
    if pat is not None:

        if pat >= 20:
            lines.append(
                "Profit grew strongly."
            )

        elif pat >= 0:
            lines.append(
                "Profit remained stable."
            )

        else:
            lines.append(
                "Profit declined."
            )

    # EBITDA
    if ebitda is not None:

        if ebitda >= 15:
            lines.append(
                "Operating performance remained healthy."
            )

        elif ebitda < 0:
            lines.append(
                "Operating margin weakened."
            )

    # EPS
    if eps is not None:

        if eps >= 15:
            lines.append(
                "EPS growth supports earnings quality."
            )

        elif eps < 0:
            lines.append(
                "EPS declined."
            )

    # Investment View
    investment = verdict.get(
        "investment",
        "Neutral"
    )

    lines.append(
        f"Investment View : {investment}"
    )

    # Risk
    risk = verdict.get(
        "risk",
        "Medium"
    )

    lines.append(
        f"Risk Level : {risk}"
    )

    # Final Verdict
    lines.append(
        f"Overall Result : {verdict.get('verdict', 'Neutral')}"
    )

    return lines
