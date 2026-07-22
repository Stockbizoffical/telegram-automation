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

    if attachment_name == "":
        return None

    # Already Full URL
    if attachment_name.lower().startswith(("http://", "https://")):
        return attachment_name

    # Remove leading slash if present
    attachment_name = attachment_name.lstrip("/")

    return BSE_PDF_BASE_URL + attachment_name


def get_pdf_url(announcement):
    """
    Extract PDF URL from a BSE announcement.
    """

    if not announcement:
        return None

    # Common BSE fields
    attachment = (
        announcement.get("ATTACHMENTNAME")
        or announcement.get("ATTACHMENT")
        or announcement.get("ATTACHMENTFILE")
        or announcement.get("PDFNAME")
        or ""
    )

    return build_pdf_url(attachment)
