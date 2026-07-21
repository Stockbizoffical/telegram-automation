import requests

URL = "https://api.bseindia.com/BseIndiaAPI/api/AnnSubCategoryGetData/w"

HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Referer": "https://www.bseindia.com/"
}

def get_bse_announcements():
    try:
        response = requests.get(URL, headers=HEADERS, timeout=20)

        if response.status_code == 200:
            return response.json()

        return []

    except Exception as e:
        print(e)
        return []
