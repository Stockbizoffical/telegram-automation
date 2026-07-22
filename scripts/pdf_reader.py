import os
import tempfile

import fitz
import pdfplumber
import requests


HEADERS = {
    "User-Agent": "StockBizAI/1.0"
}


def process_pdf(pdf_url):
    """
    Download PDF
    Extract Text using PyMuPDF
    Fallback to pdfplumber
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

        # ==========================
        # Primary : PyMuPDF
        # ==========================

        try:

            doc = fitz.open(pdf_path)

            print(f"📑 Total Pages : {len(doc)}")

            for page in doc:

                page_text = page.get_text("text")

                if page_text:
                    text += page_text + "\n"

            doc.close()

            print(f"✅ PyMuPDF Extracted Characters : {len(text)}")

        except Exception as e:

            print("PyMuPDF Error :", e)

        # ==========================
        # Fallback : pdfplumber
        # ==========================

        if len(text.strip()) < 100:

            print("⚠️ Falling back to pdfplumber...")

            text = ""

            with pdfplumber.open(pdf_path) as pdf:

                for page in pdf.pages:

                    page_text = page.extract_text()

                    if page_text:
                        text += page_text + "\n"

            print(f"✅ pdfplumber Extracted Characters : {len(text)}")

        return {
            "text": text,
            "pdf_path": pdf_path
        }

    except requests.exceptions.HTTPError as e:

        print("❌ HTTP Error :", e)

    except requests.exceptions.RequestException as e:

        print("❌ Download Error :", e)

    except Exception as e:

        print("❌ PDF Reader Error :", e)

    return None


def delete_temp_pdf(pdf_path):

    try:

        if pdf_path and os.path.exists(pdf_path):

            os.remove(pdf_path)

            print(f"🗑 Deleted : {pdf_path}")

    except Exception as e:

        print("Delete Error :", e)
