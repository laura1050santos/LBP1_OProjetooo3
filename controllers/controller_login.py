from models.model import p1,p2
from flask import Flask, Blueprint, render_template, request,redirect,url_for

app_login = Blueprint('app', __name__)
@app_login.route('/login')
def login():
    if request.method =='POST':
            username = request.form['username']
            password = request.form['password']

            if p1.user == username:
                if p1.senha == password:
                    redirect(url_for('/dashboard'))
                else:
                    redirect(url_for('/login_invalido'))
            else:
                redirect(url_for('/login_invalido'))

    return render_template('login.html')