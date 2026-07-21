import requests
from scripts.config import BSE_URL

def get_bse_announcements():
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    params = {
        "pageno": 1,
        "strCat": "-1",
        "strPrevDate": "",
        "strScrip": "",
        "strSearch": "P",
        "strToDate": "",
        "strType": "C",
        "subcategory": "-1"
    }

    response = requests.get(
        BSE_URL,
        headers=headers,
        params=params,
        timeout=30
    )

    return response.json()
