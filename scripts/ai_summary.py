def generate_summary(metrics):

    revenue = metrics.get("Revenue")
    pat = metrics.get("PAT")
    ebitda = metrics.get("EBITDA")
    eps = metrics.get("EPS")

    summary = []

    score = 50

    if revenue:
        summary.append("✅ Revenue data available")
        score += 10

    if pat:
        summary.append("✅ Profit data available")
        score += 15

    if ebitda:
        summary.append("✅ EBITDA reported")
        score += 10

    if eps:
        summary.append("✅ EPS disclosed")
        score += 10

    if score >= 90:
        verdict = "🟢 Strong Financial Disclosure"

    elif score >= 75:
        verdict = "🟡 Healthy Quarterly Update"

    else:
        verdict = "⚪ Limited Financial Information"

    return {

        "score": score,

        "verdict": verdict,

        "summary": summary

    }
