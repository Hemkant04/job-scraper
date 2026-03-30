import csv
import os
from config import CSV_FILE
from utils.helpers import generate_key

def load_existing_keys():
    keys = set()

    if not os.path.exists(CSV_FILE):
        return keys

    with open(CSV_FILE, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            keys.add(generate_key(row))

    return keys


def save_jobs(new_jobs):
    existing_keys = load_existing_keys()
    new_data = []

    for job in new_jobs:
        key = generate_key(job)
        if key not in existing_keys:
            new_data.append(job)

    file_exists = os.path.exists(CSV_FILE)

    with open(CSV_FILE, "a", newline="", encoding="utf-8") as f:
        fieldnames = ["job_title", "company_name", "location"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)

        if not file_exists:
            writer.writeheader()

        writer.writerows(new_data)

    print(f"Added {len(new_data)} new jobs")