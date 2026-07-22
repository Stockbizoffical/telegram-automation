"""
Stock Biz AI
Financial Result Detector
"""

KEYWORDS = [

    # Financial Results
    "financial result",
    "financial results",

    "quarterly result",
    "quarterly results",

    "annual result",
    "annual results",

    "standalone result",
    "standalone results",
    "standalone financial result",
    "standalone financial results",

    "consolidated result",
    "consolidated results",
    "consolidated financial result",
    "consolidated financial results",

    "audited result",
    "audited results",
    "audited financial result",
    "audited financial results",

    "unaudited result",
    "unaudited results",
    "unaudited financial result",
    "unaudited financial results",

    "statement of audited financial results",
    "statement of unaudited financial results",

    "result for the quarter",
    "results for the quarter",

    "quarter ended",
    "quarter ended on",

    "financial statement",
    "financial statements",

    "earnings",

    # Quarter Keywords
    "q1",
    "q2",
    "q3",
    "q4",

    # Financial Year
    "fy",
    "fy25",
    "fy26",
    "fy27",
    "fy28",

    # Board Meeting (Financial Results)
    "board meeting to consider financial results",
    "board meeting for financial results",
]


def is_financial_result(announcement):
    """
    Detect whether a BSE announcement is a Financial Result announcement.
    """

    subject = str(announcement.get("NEWSSUB", "")).lower()
    headline = str(announcement.get("HEADLINE", "")).lower()
    more = str(announcement.get("MORE", "")).lower()

    print("=" * 70)
    print("DEBUG : Financial Result Detector")
    print("NEWSSUB :", subject)
    print("HEADLINE :", headline)
    print("MORE :", more)
    print("=" * 70)

    text = f"{subject} {headline} {more}"

    for keyword in KEYWORDS:

        if keyword in text:
            print(f"✅ Matched Keyword : {keyword}")
            print("Financial Result : True")
            return True

    print("❌ Financial Result : FALSE")
    return False
