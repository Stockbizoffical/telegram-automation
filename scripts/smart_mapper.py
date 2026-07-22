"""
Stock Biz AI
Smart Financial Mapper V2
"""

import re


FINANCIAL_ALIASES = {

    "Revenue": [

        "revenue",
        "revenue from operations",
        "revenue from operation",
        "total revenue",
        "income",
        "income from operations",
        "income from operation",
        "operating revenue",
        "sales",
        "net sales",
        "gross sales",
        "turnover",
        "total income"

    ],

    "PAT": [

        "profit after tax",
        "net profit",
        "profit for the period",
        "profit for period",
        "profit for the year",
        "profit attributable",
        "profit/(loss) for the period",
        "profit (loss) for the period",
        "loss for the period",
        "profit"

    ],

    "EBITDA": [

        "ebitda",
        "operating profit",
        "operating ebitda",
        "ebit"

    ],

    "EPS": [

        "eps",
        "earning per share",
        "earnings per share",
        "basic eps",
        "diluted eps",
        "basic earning per share",
        "basic earnings per share",
        "diluted earning per share",
        "equity share"

    ]

}


def clean_key(text):

    text = str(text).lower()

    text = text.replace("\n", " ")

    text = re.sub(r"\(.*?\)", " ", text)

    text = re.sub(r"[^a-z ]", " ", text)

    text = re.sub(r"\s+", " ", text)

    return text.strip()


def normalize_dictionary(data):

    if not data:

        return {}

    normalized = {}

    for key, value in data.items():

        cleaned = clean_key(key)

        matched = False

        for standard, aliases in FINANCIAL_ALIASES.items():

            for alias in aliases:

                if alias in cleaned:

                    normalized[standard] = value

                    matched = True

                    break

            if matched:

                break

        if not matched:

            normalized[key] = value

    print("=" * 80)
    print("SMART MAPPER")

    for k, v in normalized.items():

        print(k, ":", v)

    print("=" * 80)

    return normalized
