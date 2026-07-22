from scripts.filters import get_category, get_impact_score
from scripts.storage import is_duplicate
from scripts.result_detector import is_financial_result

MIN_IMPACT_SCORE = 80


def get_valid_announcements(announcements, source="bse"):

    valid = []

    for item in announcements:

        news_id = item.get("NEWSID", "")

        subject = item.get("NEWSSUB", "")
        headline = item.get("HEADLINE", "")

        # NEWSSUB + HEADLINE दोनों पर Category Detect करें
        text = f"{subject} {headline}"

        category = get_category(text)
        score = get_impact_score(category)

        # Financial Results को हमेशा Allow करें
        if is_financial_result(item):
            category = "RESULT"
            score = 100

        print("=" * 60)
        print("Company :", item.get("SLONGNAME"))
        print("Category :", category)
        print("Impact Score :", score)
        print("Duplicate :", is_duplicate(source, news_id))
        print("Financial Result :", is_financial_result(item))
        print("=" * 60)

        # Skip Low Priority News
        if score < MIN_IMPACT_SCORE:
            continue

        # Skip Duplicate News
        if is_duplicate(source, news_id):
            continue

        item["CATEGORY"] = category
        item["IMPACT_SCORE"] = score

        valid.append(item)

    print(f"TOTAL HIGH PRIORITY : {len(valid)}")

    return valid
