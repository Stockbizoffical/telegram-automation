"""
Stock Biz AI
Professional Logger
"""

from datetime import datetime


LOG_FILE = "stockbiz.log"


def _write(level, message):
    """
    Internal Logger
    """

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    line = f"[{now}] [{level}] {message}"

    print(line)

    try:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(line + "\n")
    except Exception:
        pass


def log(message):
    _write("INFO", message)


def info(message):
    _write("INFO", message)


def warning(message):
    _write("WARNING", message)


def error(message):
    _write("ERROR", message)


def success(message):
    _write("SUCCESS", message)


def ai(message):
    _write("AI", message)


def result(message):
    _write("RESULT", message)
