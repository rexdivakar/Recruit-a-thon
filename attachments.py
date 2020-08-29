import os
from imbox import Imbox  # pip install imbox
import traceback
from datetime import date
import datetime
import shutil
from dashboard import set_mail_load

today = str(date.today())
year = int(today.split('-')[0])
month = int(today.split('-')[1])
day = int(today.split('-')[2])

with open('pas.1', 'r') as f:
    password = f.read()

host = "imap.gmail.com"
username = "testrecruitathon"
download_folder = "pdf_files"

dirpath = 'pdf_files'

shutil.rmtree('pdf_files', ignore_errors=True)
os.mkdir(dirpath)

if not os.path.isdir(download_folder):
    os.makedirs(download_folder, exist_ok=True)

mail = Imbox(host, username=username, password=password,
             ssl=True, ssl_context=None, starttls=False)
messages = mail.messages(date__on=datetime.date(
    year, month, day))  # defaults to inbox

for (uid, message) in (messages):
    mail.mark_seen(uid)

    for idx, attachment in enumerate(message.attachments):
        if attachment['content-type'][-3:] == 'pdf':
            att_fn = attachment.get('filename')
            download_path = f"{download_folder}/{att_fn}"
            print(download_path)
            with open(download_path, "wb") as fp:
                fp.write(attachment.get('content').read())


mail.logout()


print(set_mail_load())