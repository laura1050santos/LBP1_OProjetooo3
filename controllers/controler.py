from flask import Flask, render_template, Blueprint
from models.model import lst_personagem, Personagem

app_1 = Blueprint('app', __name__, template_folder='templates') 
@app_1.route('/')
def hello_word():
    return render_template('index.html')