from flask import Flask
from flask import render_template
from flask import request
from flask import request, redirect, render_template, url_for
import json
from dashboard import *
from mail import email_content
import time
from log_load import verify
from extra import write_log
from flaskext.markdown import Markdown
import atexit

from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)

Markdown(app)

scheduler = BackgroundScheduler()
scheduler.add_job(func=lambda: email_content(3,'rexdivakar@hotmail.com'), trigger="interval", minutes=1)
scheduler.start()

# Shut down the scheduler when exiting the app
atexit.register(lambda: scheduler.shutdown())


@app.route('/', methods=['GET', 'POST'])
def login():
    error = ''
    global ln_usr
    if request.method == 'POST':
        ln_usr = request.form['loginuser']
        ln_pass = request.form['loginPassword']
        if get_login_details(ln_usr, ln_pass):
            write_log('\nUsername: '+request.form['loginuser'])
            return redirect("/dashboard")
        else:
            error = 'Invalid Credentials'
            write_log('\n$Invalid Credentials by: '+request.form['loginuser'])
            return render_template('new_index.html', error=error)

    return render_template('new_index.html', error=error)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    return render_template('new_index.html', error="Please contact your admin")


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    return redirect("/")


@app.route('/dashboard', methods=['GET', 'POST'])
def dash():
    p_count = get_project_grp()
    emp_cnt = get_emp_cnt()
    salary=get_total_salary()
    notif = get_interview_schedule()
    table_data = json.loads(get_emp_details())
    write_log('# Dashboard Page Loaded')
    return render_template("dash_board.html", table_data=table_data, label=1, p_count=p_count, emp_cnt=emp_cnt, notif=notif,salary=salary)


@app.route('/incoming', methods=['GET', 'POST'])
def incoming():
    p_count = get_project_grp()
    emp_cnt = get_emp_cnt()
    salary=get_total_salary()
    notif = get_interview_schedule()
    graph_data = json.loads(graph_dashboard())
    mail_cnt = get_mail_count()
    tdy_cnt = get_tdy_mail_count()
    return render_template("dash_board.html", graph_data=graph_data, label=2, mail_cnt=mail_cnt, tdy_cnt=tdy_cnt, notif=notif,salary=salary)


@app.route('/reload', methods=['GET', 'POST'])
def reload():
    verify()
    return redirect("/incoming")


@app.route('/team_manag', methods=['GET', 'POST'])
def team_manag():
    p_count = get_project_grp()
    emp_cnt = get_emp_cnt()
    salary=get_total_salary()
    table_data = json.loads(get_emp_details())
    msg = ''
    notif = get_interview_schedule()
    return render_template("dash_board.html", table_data=table_data, label=3, p_count=p_count, emp_cnt=emp_cnt, notif=notif, msg=msg,salary=salary)


@app.route('/hiring', methods=['GET', 'POST'])
def hiring():
    notif = get_interview_schedule()
    table_data = json.loads(get_all_details())
    return render_template("dash_board.html", report="", table_data=table_data, label=4, notif=notif)


@app.route('/hiring_result', methods=['GET', 'POST'])
def hiring_result():
    table_data = json.loads(get_all_details())
    global candidate_id
    if request.method == 'POST':
        notif = get_interview_schedule()
        candidate_id = str(request.form['cand_id'])
        report = json.loads(get_user_details(candidate_id))
        preview_mail(candidate_id)
    return render_template("dash_board.html", report=report, table_data=table_data, label=4, notif=notif)


@app.route('/call_interview', methods=['GET', 'POST'])
def call_interview():
    global candidate_id
    table_data = json.loads(get_all_details())
    if request.method == 'POST':
        date = request.form['date']
        time = request.form['time']
        content = request.form['cmt']
        try:
            set_interview(candidate_id, date, time, content)
            msg = interview_mail(candidate_id)
            notif = get_interview_schedule()
        except:
            candidate_id = 0
            set_interview(candidate_id, date, time, content)
            msg = interview_mail(candidate_id)
            notif = get_interview_schedule()
    return render_template("dash_board.html", report='', msg=msg, table_data=table_data, label=4, notif=notif)


@app.route('/user_manag', methods=['GET', 'POST'])
def user_manag():
    notif = get_interview_schedule()
    return render_template("dash_board.html", label=5, msg='', notif=notif)


@app.route('/inside_signup', methods=['GET', 'POST'])
def inside_signup():
    msg = ''
    if request.method == 'POST':
        name = str(request.form['s_uname'])
        email = str(request.form['s_email'])
        pwd = str(request.form['s_pwd'])
        msg = set_user_signup(name, email, pwd)
        notif = get_interview_schedule()
    return render_template('dash_board.html', label=5, msg=msg, notif=notif)


@app.route('/change_pwd', methods=['GET', 'POST'])
def change_pwd():
    msg = ''
    if request.method == 'POST':
        uid = str(request.form['u_uid'])
        name = str(request.form['u_name'])
        pwd = str(request.form['u_pwd'])
        notif = get_interview_schedule()
        msg = set_forgot_password(uid, name, pwd)
    return render_template('dash_board.html', label=5, msg=msg, notif=notif)


@app.route('/about', methods=['GET', 'POST'])
def about():
    notif = get_interview_schedule()
    data1 = '''
I'm Student passionate in the field of computer science with excelling knowledge in programming languages. I am interested in team-working.
Being a curious learner,I cultivate the habit of learning new technologies which made me to do this application.
<p align="left">
    <a href="https://www.linkedin.com/in/aakash-b-b3379a190/" target="_blank"><img src="https://img.icons8.com/clouds/100/000000/linkedin.png" height="70px" width="70px;"/></a>
    <a href="https://github.com/aakash-cse" target="_blank"><img src="https://img.icons8.com/nolan/64/github.png"  height="50px" width="50px;"/></a>
</p>
*Talking about Personal Stuffs:*

- 🔭 I’m currently working on Deep Learning
- 🌱 I’m currently learning Tensorflow,MySQL and GraphQL
- 👯 I’m looking to collaborate on on any opensource projects or Hackathons.
- 💬 Ask me your doubts, I am happy to help;
- 📫 How to reach me: [Telegram](https://t.me/me_ak7)
- 😄 Pronouns: He
- ⚡ Fun fact: No comments

*Languages and Tools:* 
<p align="left">
  <img src="https://user-images.githubusercontent.com/42747200/46140125-da084900-c26d-11e8-8ea7-c45ae6306309.png" alt="c++" width="40" height="40"/>
  <img src="https://devicons.github.io/devicon/devicon.git/icons/python/python-original.svg" alt="python" width="40" height="40"/>
  <img src="https://www.vectorlogo.zone/logos/pocoo_flask/pocoo_flask-icon.svg" alt="flask" width="40" height="40"/>
  <img src="https://www.vectorlogo.zone/logos/google_cloud/google_cloud-icon.svg" alt="gcp" width="40" height="40"/> 
  <img src="https://www.vectorlogo.zone/logos/tensorflow/tensorflow-icon.svg" alt="tensorflow" width="40" height="40"/>
</p>

'''
    data2 = '''
Software Engineer - Python enthusiast Techie, Curious Problem Solver 🚀<br />
Currently this is the place where I build and break stuffs🤣
Beside's programming, I enjoy eating food and travelling.

<p align="left">
    <a href="https://www.linkedin.com/in/divakar-r-9b34b86b/" target="_blank"><img src="https://img.icons8.com/clouds/100/000000/linkedin.png" height="70px" width="70px;"/></a>
    <a href="https://github.com/rexdivakar" target="_blank"><img src="https://img.icons8.com/nolan/64/github.png"  height="50px" width="50px;"/></a>              
</p>

*Talking about Personal Stuffs:*

- 👨🏽‍💻 I’m currently working on something cool 😉;
- 🌱 I’m currently learning GraphQL and Deep learning; 
- 👯 I’m looking to collaborate on any opensource projects or Hackathons.
- 💬 Ask me about anything, I am happy to help;
- 📫 How to reach me: [Telegram](https://t.me/rexdivakar)
- ⚡ Fun fact: I ❤ breaking stuffs

*Languages and Tools:* 

<p align="left"><img src="https://www.vectorlogo.zone/logos/gnu_bash/gnu_bash-icon.svg" alt="bash" width="40" height="40"/> <img src="https://devicons.github.io/devicon/devicon.git/icons/csharp/csharp-original.svg" alt="csharp" width="40" height="40"/>
 <img src="https://devicons.github.io/devicon/devicon.git/icons/docker/docker-original-wordmark.svg" alt="docker" width="40" height="40"/> <img src="https://www.vectorlogo.zone/logos/pocoo_flask/pocoo_flask-icon.svg" alt="flask" width="40" height="40"/> 
 <img src="https://www.vectorlogo.zone/logos/google_cloud/google_cloud-icon.svg" alt="gcp" width="40" height="40"/> <img src="https://www.vectorlogo.zone/logos/git-scm/git-scm-icon.svg" alt="git" width="40" height="40"/>
  <img src="https://www.vectorlogo.zone/logos/apache_hadoop/apache_hadoop-icon.svg" alt="hadoop" width="40" height="40"/> <img src="https://www.vectorlogo.zone/logos/jenkins/jenkins-icon.svg" alt="jenkins" width="40" height="40"/>
   <img src="https://devicons.github.io/devicon/devicon.git/icons/linux/linux-original.svg" alt="linux" width="40" height="40"/> <img src="https://devicons.github.io/devicon/devicon.git/icons/mongodb/mongodb-original-wordmark.svg" alt="mongodb" width="40" height="40"/> <br>
   <img src="https://devicons.github.io/devicon/devicon.git/icons/mysql/mysql-original-wordmark.svg" alt="mysql" width="40" height="40"/> <img src="https://www.vectorlogo.zone/logos/opencv/opencv-icon.svg" alt="opencv" width="40" height="40"/>
    <img src="https://devicons.github.io/devicon/devicon.git/icons/oracle/oracle-original.svg" alt="oracle" width="40" height="40"/> <img src="https://devicons.github.io/devicon/devicon.git/icons/postgresql/postgresql-original-wordmark.svg" alt="postgresql" width="40" height="40"/>
     <img src="https://devicons.github.io/devicon/devicon.git/icons/python/python-original.svg" alt="python" width="40" height="40"/> <img src="https://www.vectorlogo.zone/logos/tensorflow/tensorflow-icon.svg" alt="tensorflow" width="40" height="40"/>

    
    '''

    return render_template("dash_board.html", data1=data1, data2=data2, label=6, notif=notif)


@app.route('/add_cand', methods=['GET', 'POST'])
def add_cand():
    table_data = json.loads(get_emp_details())
    p_count = get_project_grp()
    emp_cnt = get_emp_cnt()
    if request.method == 'POST':
        p_count = get_project_grp()
        c_id = request.form['id']
        salary = request.form['salary']
        pro_code = request.form['pro_code']
        notif = get_interview_schedule()
        msg = set_new_emp(c_id, pro_code, salary)
    return render_template('dash_board.html', table_data=table_data, label=3, p_count=p_count, emp_cnt=emp_cnt, notif=notif, msg=msg)


if __name__ == '__main__':
    global candidate_id
    global ln_usr
    app.run(host='127.0.0.1', port=8080, debug=True)
