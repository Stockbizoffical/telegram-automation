def table_to_dictionary(table):

    data = {}

    if not table:
        return data

    skip_keys = {

        "i", "ii", "iii", "iv", "v", "vi", "vii", "viii",
        "ix", "x", "xi", "xii", "xiii", "xiv", "xv",

        "a", "b", "c", "d", "e", "f", "g", "h",

        "1", "2", "3", "4", "5", "6", "7", "8", "9", "10",
        "11", "12", "13", "14", "15", "16", "17", "18",
        "19", "20", "21", "22", "23", "24", "25", "26",
        "27", "28", "29", "30"

    }

    for row in table:

        if not row:
            continue

        row = [clean(i) for i in row]

        row = [i for i in row if i.strip()]

        if len(row) < 2:
            continue

        key = ""

        for cell in row:

            text = cell.lower().strip()

            if text in skip_keys:
                continue

            if re.search(r"[a-z]", text):

                key = text
                break

        if key == "":
            continue

        numbers = []

        for cell in row:

            value = (
                cell.replace(",", "")
                .replace("₹", "")
                .replace("Rs.", "")
                .replace("Rs", "")
                .replace("%", "")
                .strip()
            )

            if re.fullmatch(r"-?\d+(\.\d+)?", value):

                numbers.append(value)

        if len(numbers) == 0:
            continue

        current = numbers[0]

        previous = numbers[1] if len(numbers) > 1 else None

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
