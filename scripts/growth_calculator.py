"""
Stock Biz AI
Growth Calculator V2
"""


def calculate_growth(financials):
    """
    Calculate Current, Previous and Growth %
    """

    result = {}

    metrics = [
        "Revenue",
        "PAT",
        "EBITDA",
        "EPS"
    ]

    for metric in metrics:

        current = financials.get(f"{metric}_current")
        previous = financials.get(f"{metric}_previous")

        growth = None

        if (
            current is not None
            and previous not in (None, 0)
        ):

            try:

                growth = round(
                    ((current - previous) / abs(previous)) * 100,
                    2
                )

            except Exception:

                growth = None

        result[metric] = {

            "current": current,

            "previous": previous,

            "growth": growth

        }

    return result
