HIGH_PRIORITY = {
    "RESULT": [
        "financial results",
        "quarterly results",
        "standalone results",
        "consolidated results",
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
        "face value",
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
def get_category(subject):

    text = subject.lower()

    # High Priority Categories
    for category, keywords in HIGH_PRIORITY.items():
        for keyword in keywords:
            if keyword in text:
                return category

    # Board Meeting Filter
    if "board meeting" in text:
        important_topics = [
            "financial results",
            "quarterly results",
            "dividend",
            "bonus",
            "buyback",
            "stock split",
            "rights",
            "qip",
            "fund raising",
        ]

        if any(topic in text for topic in important_topics):
            return "BOARD"

        return "IGNORE"

    # Low Priority / Ignore
    ignore_words = [
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
        "analyst meet",
        "investor presentation",
        "transcript",
        "certificate under regulation",
        "loss of share certificate",
    ]

    for word in ignore_words:
        if word in text:
            return "IGNORE"

    return "OTHER"
