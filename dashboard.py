import sqlite3
import json
from mail import email_content

DB = "database.sql"


def get_all_details():                    # to fetch all the user details as json format
    conn = sqlite3.connect( DB )
    conn.row_factory = sqlite3.Row
    db = conn.cursor()
    cmd='SELECT * from CANDIDATES'
    rows = db.execute(cmd).fetchall()

    conn.close()

    return json.dumps( [dict(ix) for ix in rows] )



def get_user_details(name):              # to fetch the user details 

    conn = sqlite3.connect( DB )
    conn.row_factory = sqlite3.Row
    db = conn.cursor()
    cmd='SELECT * from CANDIDATES where id='+str(name)
    rows = db.execute(cmd).fetchall()

    conn.close()

    return(json.dumps( [dict(ix) for ix in rows] ))


def interview_mail(mail_id):
    print(email_content(1,mail_id))

def preview_mail(mail_id):
    print(email_content(2,mail_id))

# preview_mail('rexdivakar@hotmail.com')