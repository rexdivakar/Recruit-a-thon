from flask import Flask,render_template,url_for,request,redirect
import json, random
app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def run_app():
	graph = {'3/5':4,'3/6':56,'3/7':4,'3/8':56}
	return render_template('home.html',graph=graph)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True) 