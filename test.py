import sqlite3
import json

DB = 'database.sql'


def set_new_emp(usr_id,pr_code, salary):
    try:
        conn = sqlite3.connect(DB)
        db = conn.cursor()
        op=json.loads(candidate_pulldb(usr_id))[0]
        name=op['NAME']
        email=op['EMAIL']
        mob_no=op['MOBILE_NO']
        skills=op['SKILLS']
        colg_name=op['COLLEGE_NAME'] 
        qualification=op['QUALIFICATION']
        designation=op['DESIGNATION']
        yrs_emp=op['YEARS_OF_EXP']
        cmd = 'insert into EMPLOYEES(name,project_code,salary,email,mobile_no,skills,college_name,QUALIFICATION,DESIGNATION,YEARS_OF_EXP,LAST_UPDATED_DATE)  values(?,?,?,?,?,?,?,?,?,?,DATE("now"))'
        db.execute(cmd,(name,pr_code,salary,email,mob_no,skills,colg_name,qualification,designation,yrs_emp))
        conn.commit()
        return 'Success !'
    except:
        return 'Insert Failed !'
    finally:
        conn.close()


def candidate_pulldb(usr_id):
    try:
        conn = sqlite3.connect(DB)
        conn.row_factory = sqlite3.Row
        db = conn.cursor()
        cmd = 'select name,email,mobile_no,skills,college_name,qualification,designation,EXPERIENCE ,company_name,years_of_exp from CANDIDATES where id=?'
        rows = db.execute(cmd, (usr_id)).fetchall()
        return json.dumps([dict(ix) for ix in rows])
    except:
        return None
    finally:
        conn.close()

