# job_scraper.py
import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_jobs(query="Python Developer", location="Chennai"):
    url = f"https://www.indeed.com/jobs?q={query}&l={location}"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    jobs = []
    for job_card in soup.select(".job_seen_beacon")[:10]:  # limit to 10 for demo
        title = job_card.select_one("h2 span")
        company = job_card.select_one(".companyName")
        location = job_card.select_one(".companyLocation")
        summary = job_card.select_one(".job-snippet")

        jobs.append({
            "Title": title.text.strip() if title else None,
            "Company": company.text.strip() if company else None,
            "Location": location.text.strip() if location else None,
            "Summary": summary.text.strip() if summary else None
        })

    df = pd.DataFrame(jobs)
    df.to_excel("jobs.xlsx", index=False)
    print("✅ Job data saved to jobs.xlsx")

if __name__ == "__main__":
    scrape_jobs()
