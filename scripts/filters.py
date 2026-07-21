RESULT_KEYWORDS = [
    "Financial Results",
    "Standalone Financial Results",
    "Consolidated Financial Results",
    "Quarterly Results",
    "Audited Financial Results",
    "Unaudited Financial Results",
]

DIVIDEND_KEYWORDS = [
    "Dividend",
]

BONUS_KEYWORDS = [
    "Bonus",
]

SPLIT_KEYWORDS = [
    "Split",
    "Stock Split",
    "Sub-Division",
]

BOARD_KEYWORDS = [
    "Board Meeting",
]

BULK_KEYWORDS = [
    "Bulk Deal",
    "Block Deal",
]


def contains_keyword(text, keywords):
    text = text.lower()

    for keyword in keywords:
        if keyword.lower() in text:
            return True

    return False


def get_category(subject):

    if contains_keyword(subject, RESULT_KEYWORDS):
        return "RESULT"

    if contains_keyword(subject, DIVIDEND_KEYWORDS):
        return "DIVIDEND"

    if contains_keyword(subject, BONUS_KEYWORDS):
        return "BONUS"

    if contains_keyword(subject, SPLIT_KEYWORDS):
        return "SPLIT"

    if contains_keyword(subject, BOARD_KEYWORDS):
        return "BOARD"

    if contains_keyword(subject, BULK_KEYWORDS):
        return "BULK"

    return "OTHER"
