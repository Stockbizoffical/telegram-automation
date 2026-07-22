"""
Stock Biz AI
Advanced Table Parser
"""

import pdfplumber


def extract_tables(pdf_path):
    """
    Extract all tables from PDF
    """

    all_tables = []

    try:

        with pdfplumber.open(pdf_path) as pdf:

            for page in pdf.pages:

                tables = page.extract_tables()

                if tables:

                    all_tables.extend(tables)

    except Exception as e:

        print(f"Table Extraction Error : {e}")

    return all_tables


def table_to_dictionary(table):
    """
    Convert Table into Dictionary
    """

    data = {}

    if not table:
        return data

    for row in table:

        if not row:
            continue

        row = [str(x).strip() if x else "" for x in row]

        key = row[0]

        if not key:
            continue

        values = row[1:]

        data[key] = values

    return data


def get_financial_tables(tables):
    """
    Return only financial tables
    """

    financial_tables = []

    keywords = [

        "income",

        "revenue",

        "sales",

        "profit",

        "expense",

        "ebitda",

        "eps",

        "operations",

        "tax"

    ]

    for table in tables:

        text = " ".join(

            str(cell).lower()

            for row in table

            for cell in row

            if cell

        )

        if any(word in text for word in keywords):

            financial_tables.append(table)

    return financial_tables
