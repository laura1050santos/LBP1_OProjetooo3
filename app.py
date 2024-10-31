from flask import Flask, request,session,render_template
from controllers.controller import loginController
from datetime import timedelta


app = Flask(__name__)
app.register_blueprint(loginController)

app.secret_key = 'chave'
app.config['permanent_session_lifetime'] = timedelta(minutes=5)
app.config['SESSION_COOKIE_SECURE']=True


@app.after_request
def log_request_info():
    print(f'Método: {request.method}, URL: {request.url}')

#paginas de erro
@app.errorhandler(404)
def erro404(e):
   return render_template('404.html'), 404

if __name__ == "__main__":
    app.run(debug=True)


#ordem que as coisas foram feitas. Login, sessão,  middleware, flash mensagers e cookies.