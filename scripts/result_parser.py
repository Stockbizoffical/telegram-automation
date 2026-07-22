import re


def clean_number(value):

    if not value:
        return None

    return (
        str(value)
        .replace(",", "")
        .replace("₹", "")
        .replace("Rs.", "")
        .strip()
    )


def extract_metrics(text):

    data = {}

    patterns = {

        "Revenue": [
            r"Revenue\s+from\s+Operations.*?([\d,]+\.\d+|[\d,]+)",
            r"Revenue.*?([\d,]+\.\d+|[\d,]+)",
            r"Total\s+Income.*?([\d,]+\.\d+|[\d,]+)",
            r"Income\s+from\s+Operations.*?([\d,]+\.\d+|[\d,]+)"
        ],

        "PAT": [
            r"Profit\s+After\s+Tax.*?([\d,]+\.\d+|[\d,]+)",
            r"Net\s+Profit.*?([\d,]+\.\d+|[\d,]+)",
            r"Profit\s+for\s+the\s+Period.*?([\d,]+\.\d+|[\d,]+)"
        ],

        "EBITDA": [
            r"EBITDA.*?([\d,]+\.\d+|[\d,]+)"
        ],

        "EPS": [
            r"Earnings\s+Per\s+Share.*?([\d,]+\.\d+|[\d,]+)",
            r"EPS.*?([\d,]+\.\d+|[\d,]+)"
        ]
    }

    for metric, regex_list in patterns.items():

        data[metric] = None

        for regex in regex_list:

            match = re.search(
                regex,
                text,
                re.IGNORECASE | re.DOTALL
            )

            if match:

                data[metric] = clean_number(
                    match.group(1)
                )

                break

    print("=" * 80)
    print("EXTRACT METRICS")
    print(data)
    print("=" * 80)

    return data
