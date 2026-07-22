"""
Stock Biz AI
Smart Financial Mapper
"""

FINANCIAL_KEYWORDS = {
    "Revenue": [
        "Revenue",
        "Revenue from Operations",
        "Income from Operations",
        "Operating Revenue",
        "Operating Income",
        "Total Income",
        "Net Sales",
        "Sales",
    ],
    "PAT": [
        "Profit After Tax",
        "Net Profit",
        "Profit for the Period",
        "Profit After Taxation",
        "PAT",
    ],
    "EBITDA": [
        "EBITDA",
        "Operating Profit",
        "EBIT",
    ],
    "EPS": [
        "EPS",
        "Basic EPS",
        "Diluted EPS",
        "Earnings Per Share",
    ],
}


def normalize_key(key):
    """Convert different financial labels to standard names."""

    key = str(key).strip().lower()

    for standard_name, aliases in FINANCIAL_KEYWORDS.items():
        for alias in aliases:
            if alias.lower() == key:
                return standard_name

    return str(key).strip()


def normalize_dictionary(financial_data):
    """Normalize all dictionary keys."""

    normalized = {}

    for key, value in financial_data.items():
        new_key = normalize_key(key)
        normalized[new_key] = value

    return normalized
