def table_to_dictionary(table):
    """
    Convert Financial Table into Dictionary
    """

    data = {}

    if not table:
        return data

    for row in table:

        if not row:
            continue

        # Clean Row
        row = [
            str(cell).replace("\n", " ").strip()
            if cell else ""
            for cell in row
        ]

        if len(row) < 3:
            continue

        key = row[0].strip()

        if key == "":
            continue

        current = row[1].strip() if len(row) > 1 else None
        previous = row[-1].strip() if len(row) > 2 else None

        # Ignore Empty Rows
        if current == "" and previous == "":
            continue

        data[key] = {
            "Current": current,
            "Previous": previous
        }

    print("=" * 80)
    print("TABLE TO DICTIONARY")
    for k, v in data.items():
        print(k, ":", v)
    print("=" * 80)

    return data
