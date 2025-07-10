from validator import is_valid_case_number
from scraper import fetch_case_html

if __name__ == "__main__":
    case_number = input("Enter your case number: ")

    if is_valid_case_number(case_number):
        print("Searching... ")

        html = fetch_case_html(case_number)

        if html:
            print("✅ HTML fetched successfully.")
            print(html[:1000])  # just print the first part of the page
        else:
            print("❌ No HTML returned.")
    else:
        print("Invalid case nubmer")