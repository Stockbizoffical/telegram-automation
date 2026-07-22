import requests
import pdfplumber
import tempfile


def extract_pdf_text(pdf_url):

    try:

        response = requests.get(pdf_url, timeout=30)

        response.raise_for_status()

        with tempfile.NamedTemporaryFile(suffix=".pdf") as temp:

            temp.write(response.content)
            temp.flush()

            text = ""

            with pdfplumber.open(temp.name) as pdf:

                for page in pdf.pages:

                    page_text = page.extract_text()

                    if page_text:
                        text += page_text + "\n"

            return text

    except Exception as e:

        print(f"PDF Error : {e}")

        return ""
