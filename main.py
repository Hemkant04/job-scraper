from scraper.jobs_scraper import scrape_jobs
from storage.csv_handler import save_jobs
from datetime import datetime

def main():
    jobs = scrape_jobs()
    print(f"Scraped {len(jobs)} jobs")

    save_jobs(jobs)



with open("/Users/hemkantsah/job_scraper/cron_check.txt", "a") as f:
    f.write(f"Ran at: {datetime.now()}\n")

if __name__ == "__main__":
    main()