import os
import tempfile

import pdfplumber
import requests


def process_pdf(pdf_url):
    """
    Download PDF
    Extract Text
    Return Text + Local PDF Path
    """

    try:

        response = requests.get(pdf_url, timeout=30)
        response.raise_for_status()

        temp = tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".pdf"
        )

        temp.write(response.content)
        temp.close()

        pdf_path = temp.name

        text = ""

        with pdfplumber.open(pdf_path) as pdf:

            for page in pdf.pages:

                page_text = page.extract_text()

                if page_text:
                    text += page_text + "\n"

        return {

            "text": text,

            "pdf_path": pdf_path

        }

    except Exception as e:

        print(f"PDF Reader Error : {e}")

        return None


def delete_temp_pdf(pdf_path):

    try:

        if os.path.exists(pdf_path):
            os.remove(pdf_path)

    except Exception as e:

        print(e)
