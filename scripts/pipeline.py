"""
Stock Biz AI
Pipeline Module
"""

from scripts.pdf_reader import process_pdf, delete_temp_pdf
from scripts.result_parser import extract_metrics
from scripts.ai_summary import generate_summary
from scripts.table_parser import extract_tables, table_to_dictionary


def analyze_pdf(pdf_url):
    """
    Complete PDF Analysis Pipeline
    """

    # Download PDF + Extract Text
    pdf = process_pdf(pdf_url)

    if not pdf:
        return None

    text = pdf["text"]
    pdf_path = pdf["pdf_path"]

    # Extract Metrics
    metrics = extract_metrics(text)

    # AI Summary
    ai = generate_summary(metrics)

    # Extract Tables
    tables = extract_tables(pdf_path)

    financial_data = {}

    if tables:

        try:
            financial_data = table_to_dictionary(tables[0])

        except Exception as e:
            print(f"Table Parser Error: {e}")

    # Delete Temporary PDF
    delete_temp_pdf(pdf_path)

    return {

        "metrics": metrics,

        "financial_data": financial_data,

        "ai": ai

    }
