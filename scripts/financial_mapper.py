"""
Stock Biz AI
Financial Mapper
"""


KEYWORDS = {

    "revenue": [
        "revenue",
        "revenue from operations",
        "total income",
        "income"
    ],

    "ebitda": [
        "ebitda",
        "operating profit"
    ],

    "pat": [
        "profit after tax",
        "net profit",
        "profit for the period"
    ],

    "eps": [
        "eps",
        "earning per share",
        "earnings per share"
    ]

}


def normalize(text):

    if text is None:
        return ""

    return str(text).strip().lower()


def map_financial_data(financial_data):

    result = {}

    if not financial_data:
        return result

    for metric, aliases in KEYWORDS.items():

        for alias in aliases:

            for row_name, row_value in financial_data.items():

                if alias in normalize(row_name):

                    if isinstance(row_value, dict):

                        result[f"{metric}_current"] = row_value.get(
                            "Current"
                        )

                        result[f"{metric}_previous"] = row_value.get(
                            "Previous"
                        )

                    elif isinstance(row_value, list):

                        if len(row_value) > 0:
                            result[f"{metric}_current"] = row_value[0]

                        if len(row_value) > 1:
                            result[f"{metric}_previous"] = row_value[1]

                    else:

                        result[f"{metric}_current"] = row_value

                    break

            if f"{metric}_current" in result:
                break

    return result
