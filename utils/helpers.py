def clean(text):
    return text.strip().replace("\n", "").lower()

def generate_key(job):
    return f"{clean(job['job_title'])}|{clean(job['company_name'])}|{clean(job['location'])}"