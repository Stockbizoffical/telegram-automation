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

        # केवल Financial Results Filter करें
        financial_results = []

        keywords = [
            "financial result",
            "financial results",
            "result",
            "results",
            "quarter",
            "quarterly",
            "audited",
            "unaudited",
            "standalone",
            "consolidated"
        ]

        for item in announcements:

            text = (
                str(item.get("HEADLINE", "")) + " " +
                str(item.get("CATEGORYNAME", "")) + " " +
                str(item.get("SUBCATNAME", ""))
            ).lower()

            if any(keyword in text for keyword in keywords):
                financial_results.append(item)

        print(f"FINANCIAL RESULTS : {len(financial_results)}")

        if financial_results:

            print("\nFIRST FINANCIAL RESULT")
            print("=" * 60)

            first = financial_results[0]

            for key, value in first.items():
                print(f"{key} : {value}")

            print("=" * 60)

        return financial_results

    except Exception as e:

        print(f"❌ ERROR : {e}")
        return []
