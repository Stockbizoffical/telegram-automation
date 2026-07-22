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

    for key, aliases in KEYWORDS.items():

        for alias in aliases:

            for row_name, row_value in financial_data.items():

                if alias in normalize(row_name):

                    result[key] = row_value

                    break

            if key in result:
                break

    return result
