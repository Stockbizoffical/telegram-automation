"""
Stock Biz AI
Automatic Pipeline Test
"""

import os
import sys

# Project Root Path
sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)

from scripts.pipeline import analyze_pdf
from scripts.bse import get_bse_announcements
from scripts.pdf_url_builder import get_pdf_url


def run_test(pdf_url):

    print("=" * 60)
    print("🚀 Stock Biz AI - Pipeline Test")
    print("=" * 60)

    if not pdf_url:
        print("❌ No PDF URL Found.")
        return

    try:

        result = analyze_pdf(pdf_url)

    except Exception as e:

        print(f"\n❌ Pipeline Error : {e}")
        return

    if not result:

        print("\n❌ Pipeline Failed")
        return

    print("\n✅ Pipeline Executed Successfully\n")

    tests = {

        "Metrics": result.get("metrics"),

        "Regex Financials": result.get("regex_financials"),

        "Table Financials": result.get("table_financials"),

        "Merged Financials": result.get("financials"),

        "Growth": result.get("growth"),

        "Trend": result.get("trend"),

        "Quality": result.get("quality"),

        "Score": result.get("score"),

        "AI Engine": result.get("ai_engine"),

    }

    passed = 0
    total = len(tests)

    print("-" * 60)

    for name, value in tests.items():

        if value:

            print(f"✅ {name}")

            passed += 1

        else:

            print(f"❌ {name}")

    print("-" * 60)

    accuracy = round((passed / total) * 100, 2)

    print(f"\n📊 Passed   : {passed}/{total}")
    print(f"🎯 Accuracy : {accuracy}%")

    if accuracy >= 90:

        print("🟢 Status : Excellent")

    elif accuracy >= 75:

        print("🟡 Status : Good")

    elif accuracy >= 50:

        print("🟠 Status : Needs Improvement")

    else:

        print("🔴 Status : Critical")

    print("=" * 60)


if __name__ == "__main__":

    print("=" * 60)
    print("🚀 Stock Biz AI Automatic Test")
    print("=" * 60)

    try:

        announcements = get_bse_announcements()

        if not announcements:

            print("❌ No Financial Result Found.")
            sys.exit(1)

        print(f"✅ Financial Results : {len(announcements)}")

        announcement = announcements[0]

        company = (
            announcement.get("SLONGNAME")
            or announcement.get("SCRIP_CD")
            or "Unknown Company"
        )

        print(f"🏢 Company : {company}")

        pdf_url = get_pdf_url(announcement)

        if not pdf_url:

            print("❌ PDF URL Not Found.")
            sys.exit(1)

        print(f"📄 PDF : {pdf_url}")

        print("=" * 60)

        run_test(pdf_url)

    except Exception as e:

        print(f"\n❌ Test Failed : {e}")

        sys.exit(1)
