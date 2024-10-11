from flask import Flask, render_template, Blueprint
from models.model import p1,lst_users

app_inicial = Blueprint('app', __name__) 

@app_inicial.route('/')
def hello_word():
    
    return render_template('index.html')
