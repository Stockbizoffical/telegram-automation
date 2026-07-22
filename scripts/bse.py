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

        r = requests.get(
            URL,
            headers=HEADERS,
            params=params,
            timeout=20
        )

        print("=" * 60)
        print("STATUS CODE:", r.status_code)
        print("REQUEST URL:", r.url)
        print("=" * 60)
        print("RESPONSE:")
        print(r.text[:2000])
        print("=" * 60)

        if r.status_code != 200:
            return []

        data = r.json()

        print("JSON KEYS:", data.keys())

        if "Table" in data and data["Table"]:

            print("TOTAL RECORDS:", len(data["Table"]))

            print("\nFIRST ANNOUNCEMENT")
            print("=" * 60)

            first = data["Table"][0]

            for key, value in first.items():
                print(f"{key} : {value}")

            print("=" * 60)

            return data["Table"]

        return []

    except Exception as e:

        print("ERROR:", str(e))
        return []
