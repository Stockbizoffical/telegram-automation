import os
import tempfile

import pdfplumber
import requests


HEADERS = {
    "User-Agent": "StockBizAI/1.0"
}


def process_pdf(pdf_url):
    """
    Download PDF
    Extract Text
    Return:
        {
            "text": "...",
            "pdf_path": "..."
        }
    """

    if not pdf_url:
        print("❌ Empty PDF URL")
        return None

    try:

        print(f"📥 Downloading PDF : {pdf_url}")

        response = requests.get(
            pdf_url,
            headers=HEADERS,
            timeout=30
        )

        print(f"🌐 Status Code : {response.status_code}")

        response.raise_for_status()

        temp = tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".pdf"
        )

        temp.write(response.content)
        temp.close()

        pdf_path = temp.name

        print(f"📄 Saved : {pdf_path}")

        text = ""

        with pdfplumber.open(pdf_path) as pdf:

            print(f"📑 Total Pages : {len(pdf.pages)}")

            for page in pdf.pages:

                page_text = page.extract_text()

                if page_text:
                    text += page_text + "\n"

        if not text.strip():

            print("⚠️ No text found inside PDF.")

            return {
                "text": "",
                "pdf_path": pdf_path
            }

        print(f"✅ Extracted Characters : {len(text)}")

        return {
            "text": text,
            "pdf_path": pdf_path
        }

    except requests.exceptions.HTTPError as e:
        print(f"❌ HTTP Error : {e}")

    except requests.exceptions.RequestException as e:
        print(f"❌ Download Error : {e}")

    except Exception as e:
        print(f"❌ PDF Reader Error : {e}")

    return None


def delete_temp_pdf(pdf_path):
    """
    Delete Temporary PDF
    """

    try:

        if pdf_path and os.path.exists(pdf_path):

            os.remove(pdf_path)

            print(f"🗑 Deleted : {pdf_path}")

    except Exception as e:

        print(f"Delete Error : {e}")
