from datetime import datetime

LOG_FILE = "data/log.txt"


def log(message):

    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(LOG_FILE, "a", encoding="utf-8") as f:

        f.write(f"[{time}] {message}\n")
