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

    pdf = process_pdf(pdf_url)

    if not pdf:
        return None

    text = pdf["text"]
    pdf_path = pdf["pdf_path"]

    try:

        # -------------------------------
        # Basic Metrics
        # -------------------------------
        metrics = extract_metrics(text)

        # -------------------------------
        # Regex Financial Parser
        # -------------------------------
        regex_financials = parse_financial_result(text)

        # -------------------------------
        # AI Summary
        # -------------------------------
        ai = generate_summary(metrics)

        # -------------------------------
        # Table Parser
        # -------------------------------
        financial_data = {}
        table_financials = {}

        try:

            tables = extract_tables(pdf_path)

            print(f"Total Tables Found : {len(tables)}")

            financial_tables = get_financial_tables(tables)

            print(f"Financial Tables Found : {len(financial_tables)}")

            if financial_tables:

                best_score = -1
                best_data = {}
                best_financial_data = {}

                for table in financial_tables:

                    temp_data = table_to_dictionary(table)

                    temp_data = normalize_dictionary(temp_data)

                    mapped = map_financial_data(temp_data)

                    score = len(mapped)

                    if score > best_score:

                        best_score = score
                        best_data = mapped
                        best_financial_data = temp_data

                financial_data = best_financial_data
                table_financials = best_data

                print(f"Best Financial Table Score : {best_score}")

            else:

                print("No Financial Table Found")

        except Exception as e:

            print(f"Table Parser Error : {e}")

        # -------------------------------
        # Merge Regex + Table
        # -------------------------------
        financials = merge_financial_data(
            regex_financials,
            table_financials
        )

        # -------------------------------
        # Growth
        # -------------------------------
        growth = calculate_growth(financials)

        # -------------------------------
        # Trend
        # -------------------------------
        trend = analyze_trends(financial_data)

        # -------------------------------
        # Quality
        # -------------------------------
        quality = analyze_quality(trend)

        # -------------------------------
        # Score
        # -------------------------------
        score = calculate_financial_score(
            growth,
            quality
        )

        # -------------------------------
        # AI Engine
        # -------------------------------
        ai_engine = build_ai_engine(
            metrics=metrics,
            financials=financials,
            growth=growth,
            trend=trend,
            quality=quality,
            score=score
        )

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

        delete_temp_pdf(pdf_path)
