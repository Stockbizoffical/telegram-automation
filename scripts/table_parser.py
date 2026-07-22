"""
Stock Biz AI
Advanced Table Parser V4
"""

import pdfplumber
import re


def extract_tables(pdf_path):
    """
    Extract all tables from PDF
    """

    all_tables = []

    try:

        with pdfplumber.open(pdf_path) as pdf:

            for page in pdf.pages:

                print(f"Scanning Page : {page.page_number}")

                tables = page.extract_tables(
                    {
                        "vertical_strategy": "text",
                        "horizontal_strategy": "text",
                    }
                )

                if tables:
                    all_tables.extend(tables)

                else:

                    table = page.extract_table(
                        {
                            "vertical_strategy": "text",
                            "horizontal_strategy": "text",
                        }
                    )

                    if table:
                        all_tables.append(table)

    except Exception as e:

        print("Table Extraction Error :", e)

    print("=" * 80)
    print("Total Tables Found :", len(all_tables))
    print("=" * 80)

    return all_tables


def clean(text):

    if text is None:
        return ""

    return str(text).replace("\n", " ").strip()


def table_to_dictionary(table):

    data = {}

    if not table:
        return data

    for row in table:

        if not row:
            continue

        row = [clean(i) for i in row]

        row = [i for i in row if i != ""]

        if len(row) < 2:
            continue

        key = row[0].lower()

        numbers = []

        for item in row[1:]:

            value = item.replace(",", "")

            if re.fullmatch(r"-?\d+(\.\d+)?", value):

                numbers.append(value)

        if len(numbers) == 0:
            continue

        current = numbers[0]

        previous = numbers[-1] if len(numbers) > 1 else None

        data[key] = {

            "Current": current,

            "Previous": previous

        }

    print("=" * 80)
    print("TABLE TO DICTIONARY")

    for k, v in data.items():

        print(k, ":", v)

    print("=" * 80)

    return data


def get_financial_tables(tables):

    financial_tables = []

    keywords = [

        "particulars",
        "income",
        "total income",
        "revenue",
        "revenue from operations",
        "operations",
        "sales",
        "profit",
        "profit before tax",
        "profit after tax",
        "profit for the period",
        "profit for the year",
        "net profit",
        "pat",
        "pbt",
        "ebit",
        "ebitda",
        "earnings per share",
        "eps",
        "basic eps",
        "diluted eps",
        "expense",
        "expenses",
        "employee benefit",
        "cost of materials",
        "other expenses",
        "finance cost",
        "depreciation",
        "tax",
        "other income",
        "comprehensive income",
        "assets",
        "liabilities",
        "equity",
        "cash flow",
        "quarter ended",
        "year ended",
        "standalone",
        "consolidated",
        "unaudited",
        "audited"

    ]

    for table in tables:

        text = " ".join(

            clean(cell).lower()

            for row in table

            for cell in row

            if cell

        )

        score = 0

        for keyword in keywords:

            if keyword in text:

                score += 1

        print("Financial Table Score :", score)

        if score >= 1:

            financial_tables.append(table)

    print("=" * 80)
    print("Financial Tables Found :", len(financial_tables))
    print("=" * 80)

    return financial_tables
