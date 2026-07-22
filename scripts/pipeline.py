from scripts.pdf_reader import extract_pdf_text
from scripts.result_parser import extract_metrics
from scripts.ai_summary import generate_summary


def analyze_pdf(pdf_url):

    text = extract_pdf_text(pdf_url)

    if not text:

        return None

    metrics = extract_metrics(text)

    ai = generate_summary(metrics)

    return {

        "metrics": metrics,

        "ai": ai

    }
