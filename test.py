import schedule
import time
from mail import email_content


def job():
    email_content(3, 'rexdivakar@hotmail.com')
    print("I'm working...")


schedule.every(1).minutes.do(job)


while True:
    schedule.run_pending()
    time.sleep(1)
