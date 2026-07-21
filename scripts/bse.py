import requests
from datetime import datetime

URL = "https://api.bseindia.com/BseIndiaAPI/api/AnnSubCategoryGetData/w"

HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Referer": "https://www.bseindia.com/",
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

        data = r.json()

        if "Table" in data:
            return data["Table"]

        return []

    except Exception as e:
        print(e)
        return []
