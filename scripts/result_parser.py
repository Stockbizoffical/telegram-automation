import re


def extract_metrics(text):

    data = {}

    patterns = {

        "Revenue": [
            r"Revenue.*?([\d,]+\.\d+|[\d,]+)",
            r"Total Income.*?([\d,]+\.\d+|[\d,]+)",
            r"Income from Operations.*?([\d,]+\.\d+|[\d,]+)"
        ],

        "PAT": [
            r"Profit After Tax.*?([\d,]+\.\d+|[\d,]+)",
            r"Net Profit.*?([\d,]+\.\d+|[\d,]+)"
        ],

        "EBITDA": [
            r"EBITDA.*?([\d,]+\.\d+|[\d,]+)"
        ],

        "EPS": [
            r"EPS.*?([\d,]+\.\d+|[\d,]+)",
            r"Earnings Per Share.*?([\d,]+\.\d+|[\d,]+)"
        ]
    }

    for key, regex_list in patterns.items():

        for regex in regex_list:

            match = re.search(regex, text, re.I | re.S)

            if match:

                data[key] = match.group(1)
                break

    return data
