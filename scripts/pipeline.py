"""
Stock Biz AI
Pipeline Module
"""

from scripts.pdf_reader import process_pdf, delete_temp_pdf
from scripts.result_parser import extract_metrics
from scripts.ai_summary import generate_summary
from scripts.table_parser import (
    extract_tables,
    table_to_dictionary,
    get_financial_tables,
)
from scripts.smart_mapper import normalize_dictionary
from scripts.financial_mapper import map_financial_data
from scripts.trend_analyzer import analyze_trends
from scripts.quality_analyzer import analyze_quality
from scripts.result_pdf_parser import parse_financial_result
from scripts.growth_calculator import calculate_growth
from scripts.financial_score import calculate_financial_score
from scripts.ai_engine import build_ai_engine
from scripts.data_merger import merge_financial_data


def analyze_pdf(pdf_url):
    """
    Complete PDF Analysis Pipeline
    """

    # ---------------------------------
    # Download PDF + Extract Text
    # ---------------------------------
    pdf = process_pdf(pdf_url)

    if not pdf:
        return None

    text = pdf["text"]
    pdf_path = pdf["pdf_path"]

    try:

        # ---------------------------------
        # Extract Basic Metrics
        # ---------------------------------
        metrics = extract_metrics(text)

        # ---------------------------------
        # Parse Financial Values (Regex)
        # ---------------------------------
        regex_financials = parse_financial_result(text)

        # ---------------------------------
        # Generate AI Summary
        # ---------------------------------
        ai = generate_summary(metrics)

        # ---------------------------------
        # Extract Financial Tables
        # ---------------------------------
        financial_data = {}
        table_financials = {}

        try:

            tables = extract_tables(pdf_path)

            financial_tables = get_financial_tables(tables)

            if financial_tables:

    best_score = -1
    best_data = {}

    for table in financial_tables:

        temp_data = table_to_dictionary(table)

        temp_data = normalize_dictionary(temp_data)

        mapped = map_financial_data(temp_data)

        score = len(mapped)

        if score > best_score:

            best_score = score
            best_data = mapped
            financial_data = temp_data

    table_financials = best_data

    print(f"Best Financial Table Score : {best_score}")

                table_financials = map_financial_data(
                    financial_data
                )

            else:

                print("No Financial Table Found")

        except Exception as e:

            print(f"Table Parser Error : {e}")

        # ---------------------------------
        # Merge Regex + Table Data
        # ---------------------------------
        financials = merge_financial_data(
            regex_financials,
            table_financials
        )

        # ---------------------------------
        # Calculate Growth
        # ---------------------------------
        growth = calculate_growth(
            financials
        )

        # ---------------------------------
        # Trend Analysis
        # ---------------------------------
        trend = analyze_trends(financial_data)

        # ---------------------------------
        # Quality Analysis
        # ---------------------------------
        quality = analyze_quality(trend)

        # ---------------------------------
        # AI Financial Score
        # ---------------------------------
        score = calculate_financial_score(
            growth,
            quality
        )

        # ---------------------------------
        # Master AI Engine
        # ---------------------------------
        ai_engine = build_ai_engine(
            metrics=metrics,
            financials=financials,
            growth=growth,
            trend=trend,
            quality=quality,
            score=score
        )

        # ---------------------------------
        # Final Output
        # ---------------------------------
        return {

            "metrics": metrics,

            "regex_financials": regex_financials,

            "table_financials": table_financials,

            "financials": financials,

            "growth": growth,

            "financial_data": financial_data,

            "trend": trend,

            "quality": quality,

            "score": score,

            "ai_engine": ai_engine,

            "ai": ai

        }

    except Exception as e:

        print(f"Pipeline Error : {e}")

        return None

    finally:

        # ---------------------------------
        # Delete Temporary PDF
        # ---------------------------------
        delete_temp_pdf(pdf_path)
