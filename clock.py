from apscheduler.schedulers.blocking import BlockingScheduler               # Online backend engine scheduler for heroku
from mail import email_content

sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=1)
def timed_job():
    email_content(3,'rexdivakar@hotmail.com')
    print("EMAIL SENT TO ADMIN!")
    
timed_job()