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

    return {

        "score": score,

        "verdict": verdict,

        "summary": executive_summary,

        "investment": verdict["investment"],

        "risk": verdict["risk"]

    }


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

    if revenue is not None:

        if revenue > 15:
            lines.append(
                "Revenue growth remained strong."
            )

        elif revenue > 0:
            lines.append(
                "Revenue reported moderate growth."
            )

        else:
            lines.append(
                "Revenue declined."
            )

    if pat is not None:

        if pat > revenue:
            lines.append(
                "Profitability improved faster than revenue."
            )

        elif pat > 0:
            lines.append(
                "Profit remained stable."
            )

        else:
            lines.append(
                "Profitability weakened."
            )

    lines.append(
        f"Overall Result : {verdict['verdict']}"
    )

    return lines
