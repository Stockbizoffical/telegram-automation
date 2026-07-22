import requests
from datetime import datetime
import time
import json

URL = "https://api.bseindia.com/BseIndiaAPI/api/AnnSubCategoryGetData/w"

HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Referer": "https://www.bseindia.com/",
    "Accept": "application/json, text/plain, */*",
    "Origin": "https://www.bseindia.com",
}


def get_bse_announcements():

    today = datetime.now().strftime("%Y%m%d")

    print("=" * 60)
    print("Searching Date :", today)
    print("=" * 60)

    params = {
    "pageno": 1,
    "strCat": "-1",
    "strPrevDate": today,
    "strToDate": today,
    "strScrip": "",
    "strSearch": "P",
    "strType": "C",
    "subcategory": "-1",
}

    try:

        session = requests.Session()
        session.headers.update(HEADERS)

        response = None

        for attempt in range(3):

            try:

                response = session.get(
                    URL,
                    params=params,
                    timeout=60
                )

                response.raise_for_status()
                break

            except requests.exceptions.RequestException as e:

                print(f"Attempt {attempt + 1} Failed : {e}")

                if attempt < 2:
                    time.sleep(5)
                else:
                    raise

        print("=" * 60)
        print("STATUS CODE :", response.status_code)
        print("REQUEST URL :", response.url)
        print("=" * 60)

        data = response.json()

        print("RESPONSE KEYS :", list(data.keys()))

        print("=" * 60)
        print("RESPONSE PREVIEW")
        print("=" * 60)
        print(json.dumps(data, indent=2)[:2000])
        print("=" * 60)

        announcements = data.get("Table", [])

        print(f"TOTAL ANNOUNCEMENTS : {len(announcements)}")

        financial_results = []

        include_keywords = [
            "financial result",
            "financial results",
            "quarterly results",
            "unaudited financial results",
            "audited financial results",
            "standalone financial results",
            "consolidated financial results",
            "quarter ended",
            "results"
        ]

        skip_keywords = [
            "board meeting",
            "meeting of board",
            "intimation",
            "prior intimation",
            "notice",
            "closure of trading window",
            "investor presentation",
            "analyst meet",
            "conference call",
            "earnings call",
            "press release",
            "newspaper publication"
        ]

        for item in announcements:

            text = (
                str(item.get("HEADLINE", "")) + " " +
                str(item.get("MORE", "")) + " " +
                str(item.get("CATEGORYNAME", "")) + " " +
                str(item.get("SUBCATNAME", ""))
            ).lower()

            if any(word in text for word in skip_keywords):
                continue

            if any(word in text for word in include_keywords):
                financial_results.append(item)

        print(f"FINANCIAL RESULTS : {len(financial_results)}")

        if financial_results:

            first = financial_results[0]

            print("=" * 60)
            print("FIRST FINANCIAL RESULT")
            print("=" * 60)
            print("Company :", first.get("SLONGNAME"))
            print("Headline :", first.get("HEADLINE"))
            print("Attachment :", first.get("ATTACHMENTNAME"))
            print("=" * 60)

        else:

            print("❌ No Financial Result Found.")

        return financial_results

    except Exception as e:

        print(f"❌ ERROR : {e}")
        return []
