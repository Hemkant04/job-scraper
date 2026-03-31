from scraper.jobs_scraper import scrape_jobs
from storage.csv_handler import save_jobs
from datetime import datetime
import os

def main():
    jobs = scrape_jobs()
    print(f"Scraped {len(jobs)} jobs")

    save_jobs(jobs)


    log_path = os.path.join(os.path.dirname(__file__), "cron_check.txt")
    with open(log_path, "a") as f:
        f.write(f"Ran at: {datetime.now()}\n")



if __name__ == "__main__":
    main()