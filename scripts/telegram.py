"""
Stock Biz AI
Telegram Sender
"""

import time
import requests

from config import BOT_TOKEN, CHANNEL_ID
from scripts.logger import (
    info,
    warning,
    error,
    success,
)

API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

MAX_LENGTH = 4096


def split_message(message, limit=MAX_LENGTH):
    """
    Split Long Telegram Messages
    """

    if len(message) <= limit:
        return [message]

    parts = []

    while len(message) > limit:

        index = message.rfind("\n", 0, limit)

        if index == -1:
            index = limit

        parts.append(message[:index])

        message = message[index:]

    if message:
        parts.append(message)

    return parts


def send_message(message):
    """
    Production Ready Telegram Sender
    """

    if not message:
        warning("Empty Telegram Message")
        return False

    messages = split_message(message)

    for part in messages:

        payload = {
            "chat_id": CHANNEL_ID,
            "text": part,
            "parse_mode": "HTML",
            "disable_web_page_preview": False,
        }

        success_flag = False

        for attempt in range(3):

            try:

                response = requests.post(
                    API_URL,
                    data=payload,
                    timeout=20
                )

                # Success
                if response.status_code == 200:

                    success("Telegram Message Sent")

                    success_flag = True

                    break

                # Too Many Requests
                elif response.status_code == 429:

                    retry = response.json().get(
                        "parameters",
                        {}
                    ).get(
                        "retry_after",
                        5
                    )

                    warning(
                        f"Rate Limited. Waiting {retry} sec"
                    )

                    time.sleep(retry)

                else:

                    error(
                        f"Telegram Error {response.status_code}"
                    )

                    error(response.text)

                    time.sleep(2)

            except requests.exceptions.Timeout:

                warning("Telegram Timeout")

                time.sleep(2)

            except requests.exceptions.ConnectionError:

                warning("Network Error")

                time.sleep(2)

            except Exception as e:

                error(str(e))

                time.sleep(2)

        if not success_flag:
            return False

    info("All Telegram Messages Delivered")

    return True
