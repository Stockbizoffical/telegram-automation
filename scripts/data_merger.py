"""
Stock Biz AI
Financial Data Merger
"""


def merge_financial_data(regex_data, table_data):
    """
    Merge Regex Data and Table Data

    Priority:
    1. Regex Value
    2. Table Value
    """

    merged = {}

    keys = set()

    if regex_data:
        keys.update(regex_data.keys())

    if table_data:
        keys.update(table_data.keys())

    for key in keys:

        value = None

        # Prefer Regex Value
        if regex_data:

            value = regex_data.get(key)

            if value in ("", None, "-", "--"):
                value = None

        # Use Table Value if Regex Missing
        if value is None and table_data:

            value = table_data.get(key)

        merged[key] = value

    return merged
