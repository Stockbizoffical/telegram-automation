"""
Stock Biz AI
Growth Calculator
"""


def to_number(value):
    """
    Convert string to float
    """

    if value is None:
        return None

    try:

        value = str(value).replace(",", "").replace("₹", "").strip()

        return float(value)

    except Exception:

        return None


def growth(current, previous):
    """
    Growth Percentage
    """

    current = to_number(current)
    previous = to_number(previous)

    if current is None or previous is None:
        return None

    if previous == 0:
        return None

    return round(((current - previous) / previous) * 100, 2)


def calculate_growth(financials):
    """
    Calculate Growth Metrics
    """

    if not financials:
        return {}

    return {

        "revenue_growth": growth(
            financials.get("revenue_current"),
            financials.get("revenue_previous")
        ),

        "pat_growth": growth(
            financials.get("pat_current"),
            financials.get("pat_previous")
        ),

        "ebitda_growth": growth(
            financials.get("ebitda_current"),
            financials.get("ebitda_previous")
        ),

        "eps_growth": growth(
            financials.get("eps_current"),
            financials.get("eps_previous")
        )

    }
