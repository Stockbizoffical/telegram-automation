import json
import os

FILE_PATH = "data/last_news.json"


def load_data():
    if not os.path.exists(FILE_PATH):
        return {}

    with open(FILE_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def save_data(data):
    with open(FILE_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


def get_last_news(source):
    data = load_data()
    return data.get(source, {}).get("last_news_id", "")


def save_last_news(source, news_id):
    data = load_data()

    if source not in data:
        data[source] = {}

    data[source]["last_news_id"] = news_id

    save_data(data)
