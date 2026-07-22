from scripts.filters import get_category, get_impact_score
from scripts.storage import is_duplicate

MIN_IMPACT_SCORE = 80


def get_valid_announcements(announcements, source="bse"):

    valid = []

    for item in announcements:

        news_id = item.get("NEWSID", "")
        subject = item.get("NEWSSUB", "")

        category = get_category(subject)
        score = get_impact_score(category)

        # Ignore Low Priority News
        if score < MIN_IMPACT_SCORE:
            continue

        # Duplicate Check
        if is_duplicate(source, news_id):
            continue

        item["CATEGORY"] = category
        item["IMPACT_SCORE"] = score

        valid.append(item)

    return valid
