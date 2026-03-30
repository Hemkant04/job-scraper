import requests
from bs4 import BeautifulSoup
from config import BASE_URL, HEADERS

def scrape_jobs():
    page = 1
    jobs = []

    while True:
        url = f"{BASE_URL}?page={page}"
        response = requests.get(url, headers=HEADERS)

        if response.status_code != 200:
            break

        soup = BeautifulSoup(response.text, "html.parser")
        boxes = soup.find_all('div', class_='card-inner')

        if not boxes:
            break

        for box in boxes:
            try:
                jobs.append({
                    "company_name": box.p.text.strip(),
                    "job_title": box.h2.text.strip(),
                    "location": box.find(
                        'div',
                        class_="d-flex align-items-center pl-1 pr-1 py-1"
                    ).text.strip()
                })
            except:
                continue

        page += 1

    return jobs