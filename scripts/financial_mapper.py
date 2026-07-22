"""
Stock Biz AI
Financial Mapper
"""


def map_financial_data(financial_data):

    result = {}

    if not financial_data:
        return result

    mapping = {
        "Revenue": "revenue",
        "PAT": "pat",
        "EBITDA": "ebitda",
        "EPS": "eps"
    }

    for key, value in financial_data.items():

        if key not in mapping:
            continue

        prefix = mapping[key]

        if isinstance(value, dict):

            result[f"{prefix}_current"] = value.get("Current")
            result[f"{prefix}_previous"] = value.get("Previous")

        elif isinstance(value, list):

            if len(value) > 0:
                result[f"{prefix}_current"] = value[0]

            if len(value) > 1:
                result[f"{prefix}_previous"] = value[-1]

        else:

            result[f"{prefix}_current"] = value

    print("=" * 80)
    print("FINANCIAL MAPPER")
    print(result)
    print("=" * 80)

    return result
