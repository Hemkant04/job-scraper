import schedule
import time
from main import main

schedule.every().day.at("09:00").do(main)

while True:
    schedule.run_pending()
    time.sleep(60)