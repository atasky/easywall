import config
from flask import Flask, render_template, session, redirect, flash, request
import os
from datetime import datetime
import sys


app = Flask(__name__)


@app.route('/')
def index():
    if check_login() is True:
        return render_template('index.html')
    else:
        return login("", None)


@app.route('/login', methods=['POST'])
def login_post():
    if request.form['password'] == 'adminadmin' and request.form['username'] == 'testuser':
        session['logged_in'] = True
    else:
        flash('wrong password!')
    return redirect("/")


@app.route("/logout")
def logout():
    session['logged_in'] = False
    return redirect("/")


def login(message, messagetype):
    if messagetype != None:
        message = ""
    today = datetime.today()
    year = today.year
    return render_template('login.html', year=year, message=message)


def check_login():
    if not session.get('logged_in'):
        return False
    return True


if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    port = 5000
    host = "0.0.0.0"
    debug = True
    app.run(host, port, debug)
