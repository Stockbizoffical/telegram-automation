"""
Stock Biz AI
Financial Mapper V2
"""


KEYWORDS = {

    "revenue": [
        "revenue",
        "revenue from operations",
        "total income",
        "income from operations",
        "income",
        "sales",
        "net sales"
    ],

    "ebitda": [
        "ebitda",
        "operating profit",
        "operating profit before depreciation"
    ],

    "pat": [
        "profit after tax",
        "net profit",
        "profit for the period",
        "profit after taxation",
        "profit attributable to owners"
    ],

    "eps": [
        "eps",
        "earning per share",
        "earnings per share",
        "basic eps",
        "diluted eps"
    ]

}


def normalize(text):

    if text is None:
        return ""

    return (
        str(text)
        .strip()
        .lower()
        .replace("\n", " ")
        .replace("  ", " ")
    )


def map_financial_data(financial_data):

    result = {}

    if not financial_data:
        return result

    for row_name, row_value in financial_data.items():

        row = normalize(row_name)

        for field, aliases in KEYWORDS.items():

            if field in result:
                continue

            for alias in aliases:

                if alias in row:

                    if isinstance(row_value, list):

                        values = [
                            str(v).strip()
                            for v in row_value
                            if str(v).strip()
                        ]

                        result[field] = values

                    else:

                        result[field] = row_value

                    break

    print("Mapped Financial Fields :", list(result.keys()))

    return result
