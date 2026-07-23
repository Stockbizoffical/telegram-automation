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
]


SKIP_KEYWORDS = [

    # Board Meeting / Intimation
    "board meeting",
    "board meeting intimation",
    "meeting of the board",
    "to consider",
    "scheduled on",

    # Non Financial PDFs
    "newspaper publication",
    "press release",
    "conference call",
    "earnings call",
    "investor presentation",
    "analyst meet",
    "analyst meeting",
    "trading window",

    # Notices
    "agm",
    "egm",
    "notice",

]


def is_financial_result(announcement):
    """
    Detect whether a BSE announcement contains ACTUAL Financial Results.
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

    # --------------------------------------------------
    # Skip Board Meeting / Non Financial Announcements
    # --------------------------------------------------

    for word in SKIP_KEYWORDS:

        if word in text:

            print(f"❌ Skipped : {word}")
            print("Financial Result : False")

            return False

    # --------------------------------------------------
    # Detect Actual Financial Results
    # --------------------------------------------------

    for keyword in KEYWORDS:

        if keyword in text:

            print(f"✅ Matched Keyword : {keyword}")
            print("Financial Result : True")

            return True

    print("❌ Financial Result : False")

    return False
