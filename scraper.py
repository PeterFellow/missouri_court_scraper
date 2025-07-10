import requests

def fetch_case_html(case_number):
    url = "https://www.courts.mo.gov/casenet/cases/searchCases.do"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    payload = {
        "inputVO.caseNumber": case_number,
        "inputVO.searchType": "casenumber"
    }

    response = requests.post(url, headers=headers, data=payload)

    if response.status_code != 200:
        print("Failed to fetch case info.")
        return None

    return response.text