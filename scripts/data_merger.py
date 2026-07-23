"""
Stock Biz AI
Financial Data Merger
"""


def is_empty(value):
    """
    Check Empty Value
    """

    if value is None:
        return True

    if isinstance(value, str):

        value = value.strip()

        if value in (
            "",
            "-",
            "--",
            "NA",
            "N/A",
            "None",
            "null",
        ):
            return True

    return False


def merge_financial_data(regex_data, table_data):
    """
    Merge Regex + Table Financial Data

    Priority:
    1. Table Parser
    2. Regex Parser (Backup)
    """

    regex_data = regex_data or {}
    table_data = table_data or {}

    merged = {}

    all_keys = set(regex_data.keys()) | set(table_data.keys())

    print("=" * 80)
    print("MERGING FINANCIAL DATA")
    print("=" * 80)

    for key in sorted(all_keys):

        regex_value = regex_data.get(key)
        table_value = table_data.get(key)

        print(f"\nKEY : {key}")
        print(f"Regex : {regex_value}")
        print(f"Table : {table_value}")

        # Table Parser gets highest priority
        if not is_empty(table_value):

            merged[key] = table_value
            print("Selected : TABLE")

        elif not is_empty(regex_value):

            merged[key] = regex_value
            print("Selected : REGEX")

        else:

            merged[key] = None
            print("Selected : NONE")

    print("\n" + "=" * 80)
    print("FINAL MERGED DATA")
    print("=" * 80)

    for k, v in merged.items():
        print(f"{k} : {v}")

    print("=" * 80)

    return merged
