from flask import Flask
from controllers.controler import app_inicial
from controllers.controller_login import app_login


app = Flask(__name__)

app.register_blueprint(app_inicial)
app.register_blueprint(app_login)

if __name__ == '__main__':
    app.run(debug=True)