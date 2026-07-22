"""
Stock Biz AI
Advanced Table Parser V3
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

                print(f"Scanning Page : {page.page_number}")

                # Primary Extraction
                tables = page.extract_tables(
                    {
                        "vertical_strategy": "text",
                        "horizontal_strategy": "text",
                    }
                )

                if tables:
                    all_tables.extend(tables)

                # Backup Extraction
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

        print(f"Table Extraction Error : {e}")

    print(f"Total Tables Found : {len(all_tables)}")

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

        data[key] = row[1:]

    return data


def get_financial_tables(tables):
    """
    Return only financial tables
    """

    financial_tables = []

    keywords = [

        "income",
        "total income",
        "revenue",
        "revenue from operations",
        "operations",
        "sales",
        "profit",
        "profit before tax",
        "profit after tax",
        "pat",
        "pbt",
        "ebit",
        "ebitda",
        "eps",
        "basic eps",
        "diluted eps",
        "expense",
        "expenses",
        "finance cost",
        "other income",
        "tax",
        "assets",
        "liabilities",
        "equity",
        "cash flow",
        "comprehensive income"

    ]

    for table in tables:

        text = " ".join(

            str(cell).lower()

            for row in table

            for cell in row

            if cell

        )

        score = sum(
            1 for keyword in keywords
            if keyword in text
        )

        if score >= 3:
            financial_tables.append(table)

    print(f"Financial Tables Found : {len(financial_tables)}")

    return financial_tables
