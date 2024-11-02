from flask import Flask, render_template
from controllers.controller import loginController

app = Flask (__name__)
app.secret_key = 'sua_chave_secreta'

app.register_blueprint(loginController)

@app.errorhandler(404) #erro de pagina não encontrada
def erro404(e):
    return render_template('404.html'), 404

@app.errorhandler(401) #erro de pagina não autorizada
def erro404(e):
    return render_template('401.html'), 401

@app.errorhandler(403) #acesso negado
def page_not_found(e):
    return render_template('403.html'), 403

@app.errorhandler(500)  #erro interno no servidor
def page_not_found(e):
    return render_template('500.html'), 500

if __name__  == '__main__':
    app.run(debug=True)