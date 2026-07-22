"""
Stock Biz AI
Pipeline Module
"""

from scripts.pdf_reader import process_pdf, delete_temp_pdf
from scripts.result_parser import extract_metrics
from scripts.ai_summary import generate_summary
from scripts.table_parser import extract_tables, table_to_dictionary
from scripts.smart_mapper import normalize_dictionary
from scripts.trend_analyzer import analyze_trends
from scripts.quality_analyzer import analyze_quality
from scripts.result_pdf_parser import parse_financial_result


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

    try:

        # -----------------------------
        # Extract Financial Metrics
        # -----------------------------
        metrics = extract_metrics(text)

        # -----------------------------
        # Parse Financial Results
        # -----------------------------
        financials = parse_financial_result(text)

        # -----------------------------
        # Generate AI Summary
        # -----------------------------
        ai = generate_summary(metrics)

        # -----------------------------
        # Extract Tables
        # -----------------------------
        tables = extract_tables(pdf_path)

        financial_data = {}

        if tables:

            try:

                financial_data = table_to_dictionary(tables[0])

                financial_data = normalize_dictionary(financial_data)

            except Exception as e:

                print(f"Table Parser Error : {e}")

        # -----------------------------
        # Trend Analysis
        # -----------------------------
        trend = analyze_trends(financial_data)

        # -----------------------------
        # Quality Analysis
        # -----------------------------
        quality = analyze_quality(trend)

        return {

            "metrics": metrics,

            "financials": financials,

            "financial_data": financial_data,

            "trend": trend,

            "quality": quality,

            "ai": ai

        }

    finally:

        # Delete Temporary PDF
        delete_temp_pdf(pdf_path)
