"""
Stock Biz AI
Pipeline Test
"""

from scripts.pipeline import analyze_pdf


def run_test(pdf_url):

    print("=" * 60)
    print("Stock Biz AI Test")
    print("=" * 60)

    result = analyze_pdf(pdf_url)

    if not result:
        print("❌ Pipeline Failed")
        return

    print("✅ Pipeline Executed")

    tests = {

        "Metrics": result.get("metrics"),

        "Financials": result.get("financials"),

        "Growth": result.get("growth"),

        "Score": result.get("score"),

        "AI Engine": result.get("ai_engine"),

    }

    print()

    passed = 0
    total = len(tests)

    for name, value in tests:

        if value:

            print(f"✅ {name}")

            passed += 1

        else:

            print(f"❌ {name}")

    print()

    print("=" * 60)

    accuracy = round(
        (passed / total) * 100,
        2
    )

    print(f"Overall : {accuracy}%")

    print("=" * 60)


if __name__ == "__main__":

    pdf = input("Enter PDF URL : ")

    run_test(pdf)
