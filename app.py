from flask import Flask,render_template, url_for
from controllers.controler import app_1


app = Flask(__name__)
app.register_blueprint(app_1)


if __name__ == '__main__':
    app.run(debug=True)