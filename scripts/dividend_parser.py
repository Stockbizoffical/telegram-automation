"""
Stock Biz AI
Dividend Parser
"""

import re


def parse_dividend(text):
    """
    Parse Dividend Information from PDF Text
    """

    result = {
        "has_dividend": False,
        "dividend_type": None,
        "dividend_per_share": None,
        "record_date": None
    }

    if not text:
        return result

    # ----------------------------------
    # Normalize Text
    # ----------------------------------

    content = " ".join(text.split())

    # ----------------------------------
    # Dividend Type
    # ----------------------------------

    if re.search(r"special\s+dividend", content, re.IGNORECASE):
        result["has_dividend"] = True
        result["dividend_type"] = "Special"

    elif re.search(r"interim\s+dividend", content, re.IGNORECASE):
        result["has_dividend"] = True
        result["dividend_type"] = "Interim"

    elif re.search(r"final\s+dividend", content, re.IGNORECASE):
        result["has_dividend"] = True
        result["dividend_type"] = "Final"

    # ----------------------------------
    # Dividend Amount
    # ----------------------------------

    amount_patterns = [

        r"Rs\.?\s*([0-9]+(?:\.[0-9]+)?)\s*per\s+equity\s+share",

        r"₹\s*([0-9]+(?:\.[0-9]+)?)\s*per\s+equity\s+share",

        r"Rs\.?\s*([0-9]+(?:\.[0-9]+)?)\s*per\s+share",

        r"₹\s*([0-9]+(?:\.[0-9]+)?)\s*per\s+share",

    ]

    for pattern in amount_patterns:

        match = re.search(pattern, content, re.IGNORECASE)

        if match:

            result["dividend_per_share"] = float(match.group(1))

            break

    # ----------------------------------
    # Record Date
    # ----------------------------------

    record_match = re.search(

        r"Record Date[:\-\s]*([0-9]{1,2}[-/ ][A-Za-z]{3,9}[-/ ][0-9]{2,4})",

        content,

        re.IGNORECASE

    )

    if record_match:

        result["record_date"] = record_match.group(1).strip()

    return result
