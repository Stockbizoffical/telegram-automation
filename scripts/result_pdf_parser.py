"""
Stock Biz AI
Financial Result PDF Parser V2
"""

import re


def clean_number(value):

    if not value:
        return None

    value = (
        str(value)
        .replace(",", "")
        .replace("₹", "")
        .replace("Rs.", "")
        .strip()
    )

    try:
        return float(value)
    except:
        return value


def find_two_values(text, keywords):

    for keyword in keywords:

        pattern = (
            rf"{keyword}.*?"
            r"([\d,]+\.\d+|[\d,]+)"
            r".*?"
            r"([\d,]+\.\d+|[\d,]+)"
        )

        match = re.search(
            pattern,
            text,
            re.IGNORECASE | re.DOTALL
        )

        if match:

            return (
                clean_number(match.group(1)),
                clean_number(match.group(2))
            )

    return (None, None)


def parse_financial_result(text):

    if not text:
        return {}

    revenue_current, revenue_previous = find_two_values(
        text,
        [
            "Revenue from Operations",
            "Revenue",
            "Total Income"
        ]
    )

    pat_current, pat_previous = find_two_values(
        text,
        [
            "Profit After Tax",
            "Net Profit",
            "Profit for the period"
        ]
    )

    ebitda_current, ebitda_previous = find_two_values(
        text,
        [
            "EBITDA"
        ]
    )

    eps_current, eps_previous = find_two_values(
        text,
        [
            "EPS",
            "Earnings Per Share"
        ]
    )

    return {

        "revenue_current": revenue_current,
        "revenue_previous": revenue_previous,

        "pat_current": pat_current,
        "pat_previous": pat_previous,

        "ebitda_current": ebitda_current,
        "ebitda_previous": ebitda_previous,

        "eps_current": eps_current,
        "eps_previous": eps_previous

    }
