"""
Stock Biz AI
Growth Calculator V3
"""


def calculate_growth(financials):
    """
    Calculate Current, Previous and Growth %
    """

    result = {}

    metrics = {
        "Revenue": "revenue",
        "PAT": "pat",
        "EBITDA": "ebitda",
        "EPS": "eps"
    }

    for name, key in metrics.items():

        current = financials.get(f"{key}_current")
        previous = financials.get(f"{key}_previous")

        # Convert to float if possible
        try:
            current = float(current) if current is not None else None
        except Exception:
            current = None

        try:
            previous = float(previous) if previous is not None else None
        except Exception:
            previous = None

        growth = None

        if current is not None and previous not in (None, 0):

            try:
                growth = round(
                    ((current - previous) / abs(previous)) * 100,
                    2
                )
            except Exception:
                growth = None

        result[name] = {
            "current": current,
            "previous": previous,
            "growth": growth
        }

    print("=" * 80)
    print("Growth Calculator")
    print(result)
    print("=" * 80)

    return result
