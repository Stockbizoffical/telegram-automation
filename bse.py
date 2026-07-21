import requests

url = "https://api.bseindia.com/BseIndiaAPI/api/AnnSubCategoryGetData/w"

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

response = requests.get(url, headers=headers, params=params)

print(response.status_code)
print(response.text[:1000])
