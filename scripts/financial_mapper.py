"""
Stock Biz AI
Financial Mapper
"""


KEYWORDS = {

    "Revenue": [
        "revenue",
        "revenue from operations",
        "total income",
        "income"
    ],

    "EBITDA": [
        "ebitda",
        "operating profit"
    ],

    "PAT": [
        "profit after tax",
        "net profit",
        "profit for the period"
    ],

    "EPS": [
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

                        result[metric] = row_value

                    else:

                        result[metric] = {
                            "Current": row_value
                        }

                    break

            if metric in result:
                break

    return result
