HIGH_PRIORITY = {
    "RESULT": [
        "financial results",
        "quarterly results",
        "standalone financial results",
        "consolidated financial results",
        "audited financial results",
        "unaudited financial results",
    ],

    "DIVIDEND": [
        "dividend",
        "interim dividend",
        "final dividend",
        "special dividend",
    ],

    "BONUS": [
        "bonus issue",
        "bonus shares",
    ],

    "SPLIT": [
        "stock split",
        "sub division",
        "sub-division",
        "face value split",
    ],

    "BUYBACK": [
        "buyback",
        "buy back",
    ],

    "RIGHTS": [
        "rights issue",
    ],

    "QIP": [
        "qualified institutions placement",
        "qip",
    ],

    "BULK": [
        "bulk deal",
        "block deal",
    ],
}


IGNORE_WORDS = [
    "newspaper",
    "advertisement",
    "closure of trading window",
    "trading window",
    "shareholding pattern",
    "postal ballot",
    "scrutinizer",
    "agm",
    "egm",
    "voting result",
    "compliance certificate",
    "certificate under regulation",
    "investor presentation",
    "analyst meet",
    "conference call",
    "transcript",
    "loss of share certificate",
]


IMPORTANT_BOARD_TOPICS = [
    "financial results",
    "quarterly results",
    "dividend",
    "bonus",
    "buyback",
    "rights",
    "stock split",
    "sub division",
    "qip",
    "fund raising",
]


IMPACT_SCORE = {
    "RESULT": 100,
    "DIVIDEND": 95,
    "BONUS": 95,
    "BUYBACK": 95,
    "SPLIT": 90,
    "RIGHTS": 90,
    "QIP": 90,
    "BULK": 85,
    "BOARD": 80,
    "OTHER": 20,
    "IGNORE": 0,
}


def get_category(subject):

    text = subject.lower().strip()

    for category, keywords in HIGH_PRIORITY.items():
        for keyword in keywords:
            if keyword in text:
                return category

    if "board meeting" in text:

        for topic in IMPORTANT_BOARD_TOPICS:
            if topic in text:
                return "BOARD"

        return "IGNORE"

    for word in IGNORE_WORDS:
        if word in text:
            return "IGNORE"

    return "OTHER"


def get_impact_score(category):

    return IMPACT_SCORE.get(category, 0)
