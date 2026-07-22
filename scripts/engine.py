from scripts.filters import get_category

ALLOWED_CATEGORIES = [
    "RESULT",
    "DIVIDEND",
    "BONUS",
    "SPLIT",
    "BOARD",
    "BULK",
]


def get_valid_announcements(announcements):
    valid = []

    for item in announcements:
        subject = item.get("NEWSSUB", "")
        category = get_category(subject)

        if category in ALLOWED_CATEGORIES:
            item["CATEGORY"] = category
            valid.append(item)

    return valid
