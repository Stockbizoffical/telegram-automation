"""
Stock Biz AI
PDF URL Builder
"""

BSE_PDF_BASE_URL = "https://www.bseindia.com/xml-data/corpfiling/AttachLive/"


def build_pdf_url(attachment_name):
    """
    Convert BSE attachment filename into full PDF URL.
    """

    if not attachment_name:
        return None

    attachment_name = str(attachment_name).strip()

    # Already Full URL
    if attachment_name.lower().startswith("http"):
        return attachment_name

    return BSE_PDF_BASE_URL + attachment_name
