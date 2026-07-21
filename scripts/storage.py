import os

FILE_NAME = "last_news.txt"

def get_last_news():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            return f.read().strip()
    return ""

def save_last_news(news_id):
    with open(FILE_NAME, "w") as f:
        f.write(str(news_id))
