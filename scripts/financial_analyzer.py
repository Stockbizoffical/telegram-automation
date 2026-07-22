def calculate_growth(current, previous):

    try:
        current = float(str(current).replace(",", ""))
        previous = float(str(previous).replace(",", ""))

        if previous == 0:
            return None

        growth = ((current - previous) / previous) * 100

        return round(growth, 2)

    except:
        return None


def get_rating(growth):

    if growth is None:
        return "⚪ Unknown"

    if growth >= 25:
        return "🟢 Excellent"

    if growth >= 15:
        return "🟢 Strong"

    if growth >= 5:
        return "🟡 Positive"

    if growth >= 0:
        return "🟠 Flat"

    return "🔴 Weak"
    def calculate_score(result):

    score = 50

    revenue = result.get("Revenue Growth")
    pat = result.get("PAT Growth")
    eps = result.get("EPS Growth")

    if revenue is not None:

        if revenue > 15:
            score += 15

        elif revenue > 5:
            score += 8

    if pat is not None:

        if pat > 20:
            score += 20

        elif pat > 10:
            score += 10

    if eps is not None:

        if eps > 15:
            score += 10

    return min(score,100)
