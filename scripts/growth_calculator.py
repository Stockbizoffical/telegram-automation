"""
Stock Biz AI
Growth Calculator V4
"""


def calculate_growth(financials):
    """
    Calculate Growth %
    Returns Flat Dictionary
    """

    result = {}

    metrics = {
        "revenue": "Revenue",
        "pat": "PAT",
        "ebitda": "EBITDA",
        "eps": "EPS"
    }

    for key, title in metrics.items():

        current = financials.get(f"{key}_current")
        previous = financials.get(f"{key}_previous")

        try:
            current = float(current) if current not in (None, "") else None
        except:
            current = None

        try:
            previous = float(previous) if previous not in (None, "") else None
        except:
            previous = None

        growth = None

        if current is not None and previous not in (None, 0):

            growth = round(
                ((current - previous) / abs(previous)) * 100,
                2
            )

        result[f"{key}_current"] = current
        result[f"{key}_previous"] = previous
        result[f"{key}_growth"] = growth

    print("=" * 80)
    print("Growth Calculator V4")
    print(result)
    print("=" * 80)

    return result
