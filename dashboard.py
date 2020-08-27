import sqlite3
import json
from mail import email_content

DB = "database.sql"


def get_all_details():                    # to fetch all the user details as json format
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    db = conn.cursor()
    cmd = 'SELECT ID,NAME,SKILLS,YEARS_OF_EXP from CANDIDATES ORDER BY ID DESC'
    rows = db.execute(cmd).fetchall()

    conn.close()

    return json.dumps([dict(ix) for ix in rows])


def get_user_details(usr_id):              # to fetch the user details

    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    db = conn.cursor()
    cmd = 'SELECT * from CANDIDATES where id='+usr_id
    rows = db.execute(cmd).fetchall()

    conn.close()

    return(json.dumps([dict(ix) for ix in rows]))

def get_mail_id(usr_id):                   # To fetch the mail id from the user id
    conn = sqlite3.connect(DB)
    db = conn.cursor()
    cmd = 'SELECT EMAIL from CANDIDATES where id='+usr_id
    rows = db.execute(cmd)
    extract_id=rows.fetchmany()[0]
    mail_id=' '.join(map(str, extract_id)) 
    conn.close()

    return mail_id

def preview_mail(usr_id):                   
    email_content(1,get_mail_id(usr_id))                 # 1 to trigger the preview mail
    print('Preview Mail sent for Canidate_id: ',usr_id)

preview_mail('277')

def interview_mail(usr_id):                                   # 2 to trigger the interview mail
    print(email_content(2, get_mail_id(usr_id)))
    print('Interview Mail sent for Canidate_id: ',usr_id)
