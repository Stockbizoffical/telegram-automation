"""
Stock Biz AI
Table Parser
"""

import pdfplumber


def extract_tables(pdf_path):

    all_tables = []

    try:

        with pdfplumber.open(pdf_path) as pdf:

            for page in pdf.pages:

                tables = page.extract_tables()

                if tables:

                    for table in tables:

                        if table:
                            all_tables.append(table)

    except Exception as e:

        print(f"Table Parser Error: {e}")

    return all_tables


def table_to_dictionary(table):

    result = {}

    if len(table) < 2:
        return result

    for row in table[1:]:

        if not row or len(row) < 3:
            continue

        key = str(row[0]).strip()

        result[key] = {
            "Current": row[1],
            "Previous": row[2]
        }

    return result
