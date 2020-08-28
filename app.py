from flask import Flask
from flask import render_template
from flask import request
from flask import request,redirect,render_template,url_for
import csv
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def login():
	error=None
	if request.method == 'POST':
		if request.form['loginuser'] != 'admin' or request.form['loginPassword'] != 'admin':
			error = 'Invalid Credentials. Please try again.'
		else:
			return redirect("/dashboard")
	return render_template('fun.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
	error=None
	pass

@app.route('/dashboard',methods=['GET','POST'])
def dashboard():
	user = 'dummy_user'
	return render_template('dashboard.html',user=user)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True) 