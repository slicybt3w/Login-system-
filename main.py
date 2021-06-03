#Login system with python

from flask import Flask,request,render_template,redirect
import beedb

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/reg')
def reg():
    return render_template('reg.html')

@app.route('/pass_save',methods=["POST"])
def pass_save():
    username = request.form['username']
    password = request.form['password']
    if username in beedb.allfile():
        if password == beedb.get(f'{username}.password'):
            return username
        else:
            return "Wrong password"
    else:
        return " No account like this"
    

@app.route('/reg_save',methods=["POST"])
def reg_save():
    username = request.form['username']
    password = request.form['password']
    if username in beedb.allfile():
        return "None boy"
    else:
        beedb.set(username,{"password":password})

    return redirect('/')

app.run(debug=True)
