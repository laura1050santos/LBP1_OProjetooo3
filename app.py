from flask import Flask, request,session
from controllers.controller import loginController
from datetime import timedelta


app = Flask(__name__)

app.secret_key = 'chave'
app.permanent_session_lifetime = timedelta(minutes=5)

@app.before_request
def log_request_info():
    print(f'Método: {request.method}, URL: {request.url}')

app.register_blueprint(loginController)

if __name__ == "__main__":
    app.run(debug=True)