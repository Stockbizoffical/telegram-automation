if __name__ == "__main__":

    pdf_url = input("Enter PDF URL: ").strip()

    if not pdf_url:
        print("❌ PDF URL is required.")
    else:
        run_test(pdf_url)
