from scripts.bse import get_bse_announcements
from scripts.telegram import send_message
from scripts.storage import get_last_news, save_last_news
from scripts.formatter import format_bse_announcement
from scripts.filters import get_category

SOURCE = "bse"

# केवल ये Categories Telegram पर जाएंगी
ALLOWED_CATEGORIES = [
    "RESULT",
    "DIVIDEND",
    "BON
