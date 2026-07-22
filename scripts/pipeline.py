"""
Stock Biz AI
Pipeline Module
"""

from scripts.pdf_reader import extract_pdf_text
from scripts.result_parser import extract_metrics
from scripts.ai_summary import generate_summary
from scripts.table_parser import extract_tables, table_to_dictionary


def analyze_pdf(pdf_url):
    """
    Complete PDF Analysis Pipeline
    """

    # Extract PDF Text
    text = extract_pdf_text(pdf_url)

    if not text:
        return None

    # Extract Metrics From Text
    metrics = extract_metrics(text)

    # Generate AI Summary
    ai = generate_summary(metrics)

    # Extract Financial Tables
    tables = extract_tables(pdf_url)

    financial_data = {}

    if tables:

        try:
            financial_data = table_to_dictionary(tables[0])

        except Exception as e:
            print(f"Table Parser Error: {e}")

    return {

        "metrics": metrics,

        "financial_data": financial_data,

        "ai": ai

    }
