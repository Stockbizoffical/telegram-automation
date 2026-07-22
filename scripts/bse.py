import requests
from datetime import datetime

URL = "https://api.bseindia.com/BseIndiaAPI/api/AnnSubCategoryGetData/w"

HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Referer": "https://www.bseindia.com/",
    "Accept": "application/json, text/plain, */*",
    "Origin": "https://www.bseindia.com",
}


def get_bse_announcements():

    today = datetime.now().strftime("%Y%m%d")

    params = {
        "pageno": 1,
        "strCat": "-1",
        "strPrevDate": today,
        "strToDate": today,
        "strScrip": "",
        "strSearch": "P",
        "strType": "C",
        "subcategory": "",
    }

    try:

        response = requests.get(
            URL,
            headers=HEADERS,
            params=params,
            timeout=20
        )

        print("=" * 60)
        print("STATUS CODE :", response.status_code)
        print("REQUEST URL :", response.url)
        print("=" * 60)

        if response.status_code != 200:
            print("❌ Failed to fetch announcements.")
            return []

        data = response.json()

        announcements = data.get("Table", [])

        print(f"TOTAL ANNOUNCEMENTS : {len(announcements)}")

        financial_results = []

        # Result Keywords
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

        # Skip Keywords
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

            # Skip unwanted announcements
            if any(word in text for word in skip_keywords):
                continue

            # Keep only financial results
            if any(word in text for word in include_keywords):
                financial_results.append(item)

        print(f"FINANCIAL RESULTS : {len(financial_results)}")

        if financial_results:

            print("\nFIRST FINANCIAL RESULT")
            print("=" * 60)

            first = financial_results[0]

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
