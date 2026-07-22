"""
Stock Biz AI
Financial Result Detector
"""


KEYWORDS = [

    "financial results",
    "quarterly results",
    "annual results",
    "standalone results",
    "consolidated results",
    "audited financial results",
    "unaudited financial results",
    "earnings",
    "q1",
    "q2",
    "q3",
    "q4",
    "fy",
    "board meeting"

]


def is_financial_result(announcement):

    subject = str(announcement.get("NEWSSUB", "")).lower()

    headline = str(announcement.get("HEADLINE", "")).lower()

    more = str(announcement.get("MORE", "")).lower()

    text = subject + " " + headline + " " + more

    for keyword in KEYWORDS:

        if keyword in text:
            return True

    return False
