import json
import os

FILE_PATH = "data/last_news.json"

MAX_NEWS_IDS = 1000


def load_data():
    if not os.path.exists(FILE_PATH):
        return {}

    with open(FILE_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def save_data(data):
    with open(FILE_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


def get_processed_news(source):

    data = load_data()

    return data.get(source, {}).get("processed_news", [])


def is_duplicate(source, news_id):

    processed = get_processed_news(source)

    return news_id in processed


def save_news(source, news_id):

    data = load_data()

    if source not in data:
        data[source] = {}

    processed = data[source].get("processed_news", [])

    processed.append(news_id)

    # केवल अंतिम 1000 News IDs रखें
    processed = processed[-MAX_NEWS_IDS:]

    data[source]["processed_news"] = processed

    save_data(data)
