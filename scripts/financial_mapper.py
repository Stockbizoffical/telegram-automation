"""
Stock Biz AI
Smart Financial Mapper V2
"""


def map_financial_data(financial_data):

    result = {}

    if not financial_data:
        return result

    for key, value in financial_data.items():

        k = str(key).lower().strip()

        prefix = None

        # ---------------- Revenue ----------------

        if (
            "revenue from operations" in k
            or "revenue" in k
            or "total income" in k
            or "income from operations" in k
            or "net sales" in k
            or "sales" in k
        ):
            prefix = "revenue"

        # ---------------- PAT ----------------

        elif (
            "profit after tax" in k
            or "net profit" in k
            or "profit for the period" in k
            or "profit for the year" in k
            or "pat" == k
        ):
            prefix = "pat"

        # ---------------- EBITDA ----------------

        elif (
            "ebitda" in k
            or "ebit" == k
            or "operating profit" in k
        ):
            prefix = "ebitda"

        # ---------------- EPS ----------------

        elif (
            "earnings per share" in k
            or "basic eps" in k
            or "diluted eps" in k
            or "eps" == k
        ):
            prefix = "eps"

        if not prefix:
            continue

        if isinstance(value, dict):

            result[f"{prefix}_current"] = value.get("Current")
            result[f"{prefix}_previous"] = value.get("Previous")

        elif isinstance(value, list):

            if len(value) > 0:
                result[f"{prefix}_current"] = value[0]

            if len(value) > 1:
                result[f"{prefix}_previous"] = value[1]

        else:

            result[f"{prefix}_current"] = value

    print("=" * 80)
    print("SMART FINANCIAL MAPPER")
    print(result)
    print("=" * 80)

    return result
