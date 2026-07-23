"""
Stock Biz AI
Financial Result PDF Parser V3
"""

import re


def clean_number(value):
    if not value:
        return None

    value = str(value).strip()

    # Negative values like (123.45)
    if value.startswith("(") and value.endswith(")"):
        value = "-" + value[1:-1]

    value = (
        value.replace(",", "")
        .replace("₹", "")
        .replace("Rs.", "")
        .replace("Rs", "")
        .replace("%", "")
        .replace("*", "")
        .replace("#", "")
        .replace("^", "")
        .strip()
    )

    try:
        return float(value)
    except:
        return None


def find_values(text, keywords):

    number_pattern = r"\(?-?\d[\d,]*\.?\d*\)?"

    for keyword in keywords:

        pattern = (
            rf"{re.escape(keyword)}"
            rf"[\s\S]{{0,250}}?"
            rf"({number_pattern})"
            rf"[\s\S]{{0,80}}?"
            rf"({number_pattern})"
        )

        matches = re.finditer(
            pattern,
            text,
            re.IGNORECASE
        )

        for match in matches:

            current = clean_number(match.group(1))
            previous = clean_number(match.group(2))

            if current is not None:
                return current, previous

    return None, None


def parse_financial_result(text):

    if not text:
        return {}

    revenue_current, revenue_previous = find_values(
        text,
        [
            "Revenue from Operations",
            "Revenue from Contracts with Customers",
            "Revenue",
            "Total Income",
            "Operating Revenue",
            "Income from Operations",
            "Net Sales",
            "Sales",
            "Turnover",
        ]
    )

    pat_current, pat_previous = find_values(
        text,
        [
            "Profit After Tax",
            "Net Profit",
            "Profit for the Period",
            "Profit for the Year",
            "PAT",
        ]
    )

    ebitda_current, ebitda_previous = find_values(
        text,
        [
            "EBITDA",
            "Operating Profit",
            "EBIT",
        ]
    )

    eps_current, eps_previous = find_values(
        text,
        [
            "Earnings Per Share",
            "Basic EPS",
            "Diluted EPS",
            "EPS",
        ]
    )

    result = {
        "revenue_current": revenue_current,
        "revenue_previous": revenue_previous,
        "pat_current": pat_current,
        "pat_previous": pat_previous,
        "ebitda_current": ebitda_current,
        "ebitda_previous": ebitda_previous,
        "eps_current": eps_current,
        "eps_previous": eps_previous,
    }

    print("=" * 80)
    print("REGEX FINANCIAL PARSER")
    print(result)
    print("=" * 80)

    return result
