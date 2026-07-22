"""
Stock Biz AI
Financial Data Merger
"""


def is_empty(value):

    return value in (
        None,
        "",
        "-",
        "--",
        "NA",
        "N/A"
    )


def merge_financial_data(regex_data, table_data):
    """
    Merge Regex + Table Financial Data

    Priority:
    1. Regex
    2. Table
    """

    regex_data = regex_data or {}
    table_data = table_data or {}

    merged = {}

    all_keys = set(regex_data.keys()) | set(table_data.keys())

    for key in all_keys:

        regex_value = regex_data.get(key)
        table_value = table_data.get(key)

        if not is_empty(regex_value):

            merged[key] = regex_value

        elif not is_empty(table_value):

            merged[key] = table_value

        else:

            merged[key] = None

    print("=" * 80)
    print("MERGED FINANCIAL DATA")
    for k, v in merged.items():
        print(f"{k} : {v}")
    print("=" * 80)

    return merged
