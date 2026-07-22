"""
Stock Biz AI
Financial Result PDF Parser
"""

import re


PATTERNS = {
    "revenue": [
        r"Revenue\s*from\s*Operations\s*[:\-]?\s*([\d,]+\.\d+|[\d,]+)",
        r"Total\s*Income\s*[:\-]?\s*([\d,]+\.\d+|[\d,]+)",
    ],
    "ebitda": [
        r"EBITDA\s*[:\-]?\s*([\d,]+\.\d+|[\d,]+)",
    ],
    "pat": [
        r"Profit\s*After\s*Tax\s*[:\-]?\s*([\d,]+\.\d+|[\d,]+)",
        r"Net\s*Profit\s*[:\-]?\s*([\d,]+\.\d+|[\d,]+)",
    ],
    "eps": [
        r"EPS\s*[:\-]?\s*([\d,]+\.\d+|[\d,]+)",
        r"Earnings\s*Per\s*Share\s*[:\-]?\s*([\d,]+\.\d+|[\d,]+)",
    ],
}


def clean_value(value):
    """Remove commas and spaces."""

    if not value:
        return None

    value = value.replace(",", "").strip()

    return value


def find_value(text, patterns):

    for pattern in patterns:

        match = re.search(pattern, text, re.IGNORECASE)

        if match:

            return clean_value(match.group(1))

    return None


def parse_financial_result(text):

    if not text:
        return {}

    result = {}

    for key, patterns in PATTERNS.items():

        result[key] = find_value(text, patterns)

    return result
