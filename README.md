# JobsNepal Web Scraper

A Python-based web scraping project that extracts job listings from JobsNepal, stores them in a CSV file, and automatically updates daily without duplicates.


## Features

- Scrapes job listings from JobsNepal
- Extracts:
    - Job Title
    - Company Name
    - Location
- Handles multiple pages (pagination)
- Stores data in CSV format
- Prevents duplicate entries automatically
- Supports daily automation using cron job
- Clean modular project structure

## 🌐 General Use Case

This project is a working example of a web scraper that can be adapted to many similar job listing or content websites.

The same approach can be used for:

- Job portals (Indeed, Glassdoor, LinkedIn-like sites)
- E-commerce websites (product scraping, price tracking)
- News websites (article collection)
- Real estate listings
- Course platforms


###  How it can be reused

To adapt this project for another website, you typically only need to:

- Update the target URL in `config.py`
- Modify the HTML selectors in `scraper/jobs_scraper.py`
- Adjust fields based on available data (title, company, location, etc.)

The core logic (pagination, scraping loop, deduplication, and CSV storage) remains the same.


##  Key Insight

This project demonstrates a reusable scraping pipeline:

Scrape → Parse → Clean → Deduplicate → Store → Automate

This pattern can be applied to almost any structured website data extraction task.

##  Project Structure

```
job_scraper/
├── scraper/              # Web scraping logic
├── storage/              # CSV read/write handling
├── utils/                # Helper functions (cleaning, keys)
├── scheduler/            # Optional automation script
├── data/                 # Output CSV file
├── main.py               # Entry point
├── config.py             # Configuration (URLs, paths)
├── requirements.txt      # Dependencies
└── README.md
```



## Installation

### 1. Clone the project
```bash
git clone <your-repo-url>
cd job_scraper
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the scraper
```bash
python main.py
```


## Dependencies

- `requests` - HTTP requests
- `beautifulsoup4` - HTML parsing
- `pandas` - Data handling


##  Tech Stack
- Python
- BeautifulSoup (Web Scraping)
- Requests (HTTP handling)
- CSV (Data storage)
- Cron (Automation)