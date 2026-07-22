"""
Stock Biz AI
Smart Financial Mapper
"""


FINANCIAL_ALIASES = {

    "Revenue": [
        "Revenue",
        "Revenue from Operations",
        "Revenue From Operations",
        "Income from Operations",
        "Income From Operations",
        "Sales",
        "Net Sales",
        "Total Income",
        "Operating Revenue"
    ],

    "PAT": [
        "Profit After Tax",
        "Net Profit",
        "Profit for the Period",
        "Profit After Tax (PAT)",
        "Profit for period",
        "Net Profit After Tax"
    ],

    "EBITDA": [
        "EBITDA",
        "Operating Profit",
        "Operating EBITDA",
        "EBIT"
    ],

    "EPS": [
        "EPS",
        "Basic EPS",
        "Diluted EPS",
        "Earnings Per Share",
        "Basic Earnings Per Share"
    ]
}


def normalize_dictionary(data):
    """
    Normalize Financial Keys
    """

    if not data:
        return {}

    normalized = {}

    for key, value in data.items():

        key_text = str(key).strip().lower()

        found = False

        for standard_name, aliases in FINANCIAL_ALIASES.items():

            for alias in aliases:

                if alias.lower() in key_text:

                    normalized[standard_name] = value

                    found = True

                    break

            if found:
                break

        if not found:
            normalized[key] = value

    return normalized
