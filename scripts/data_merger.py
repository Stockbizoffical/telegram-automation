"""
Stock Biz AI
Financial Data Merger V2
"""


def is_empty(value):

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


def is_valid_number(value):

    if is_empty(value):
        return False

    try:

        value = str(value).replace(",", "").strip()

        float(value)

        return True

    except:

        return False


def merge_financial_data(regex_data, table_data):

    regex_data = regex_data or {}
    table_data = table_data or {}

    merged = {}

    all_keys = sorted(
        set(regex_data.keys()) |
        set(table_data.keys())
    )

    print("=" * 80)
    print("MERGING FINANCIAL DATA V2")
    print("=" * 80)

    for key in all_keys:

        regex_value = regex_data.get(key)
        table_value = table_data.get(key)

        print(f"\nKEY : {key}")
        print("Regex :", regex_value)
        print("Table :", table_value)

        # Highest Priority
        if is_valid_number(table_value):

            merged[key] = table_value
            print("Selected : TABLE")

        elif is_valid_number(regex_value):

            merged[key] = regex_value
            print("Selected : REGEX")

        elif not is_empty(table_value):

            merged[key] = table_value
            print("Selected : TABLE (TEXT)")

        elif not is_empty(regex_value):

            merged[key] = regex_value
            print("Selected : REGEX (TEXT)")

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
