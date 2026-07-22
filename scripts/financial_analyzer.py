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
