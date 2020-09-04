import sqlite3
import json
from mail import email_content
import hashlib, binascii, os

DB = "database.sql"


def hash_password(password):
    """Hash a password for storing."""
    salt = hashlib.sha256(os.urandom(30)).hexdigest().encode('ascii')
    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), 
                                salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)
    return (salt + pwdhash).decode('ascii')

def set_user_signup(usr_name,email,pass_wrd):                  
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    pass_wrd=hash_password(pass_wrd)
    cmd='insert into login_access(username,email,password) values(?,?,?)'
    cur.execute(cmd,(usr_name,email,pass_wrd))
    conn.commit()
    conn.close()
    
# set_user_signup('divakar','p@gmail.com','password')    
 
def verify_password(stored_password, provided_password):
    """Verify a stored password against one provided by user"""
    salt = stored_password[:64]
    stored_password = stored_password[64:]
    pwdhash = hashlib.pbkdf2_hmac('sha512', 
                                  provided_password.encode('utf-8'), 
                                  salt.encode('ascii'), 
                                  100000)
    pwdhash = binascii.hexlify(pwdhash).decode('ascii')
    return pwdhash == stored_password


def get_login_details(usr_name,pass_wrd):                  
    conn = sqlite3.connect(DB)
    db = conn.cursor()
    cmd = 'select password from login_access where username=?'
    rows= db.execute(cmd,(usr_name,))
    stor_dat = rows.fetchone()[0]
    
    status=verify_password(stor_dat,pass_wrd)    
    conn.close()
    return status
    
