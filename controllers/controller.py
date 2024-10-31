from flask import Blueprint, render_template, request, redirect, url_for, session, flash, abort
from models.usuario import lista_usuarios

loginController = Blueprint('login', __name__)

@loginController.route("/")
def inicial():
    return render_template("incial.html")

@loginController.route("/login", methods=['GET, POST'])
def login ():
    if request.method == 'POST':
        nome = request.form['nome'] #usa o 'name' do input pra pegar a informação do formulario
        senha = request.form.get('senha')
        for usuario in lista_usuarios:
            if usuario.nome == nome and usuario.senha == senha: #criar a session quando o usuario acertar o login, depois da validação
                session['user']= usuario.nome #não armazenar dados sensiveis como senha na sessão.
                session['iduser']= usuario.id
                return redirect(url_for('login.dashboard'))
        flash("credenciais erradas")     
        print( 'Login Inválido')    
        return redirect(url_for('login.login') ) #login(nome da blueprint).login (nome da função)
    return render_template("login.html")

@loginController.route("/dashboard")
def dashboard():
        return render_template("dashboard.html")

@loginController.route("/logout")
def logout():
    session.pop('iduser',None) #pop transforma o elemento em none, nada.
    session.pop('user', None)
    return redirect(url_for('login.inicial'))

@loginController.route("/adm")
def admin():
    if session.get['iduser'] != 1:
        abort(401)
    return "<pagina de adm> "
    

@loginController.before_request
def verificalogin(): 
    if request.endpoint =='login.login' and 'iduser' in session: #verificar primeiro se o usuario está logado 
        return redirect(url_for('login.index'))
    
    if request.endpoint in rotas_publicas: #endpoint retorna a url_for da função/// verificar depois se a rota é publica e pode ser acessada msm sem login
        return
    
    if 'iduser' not in session:
        return redirect(url_for('login.login'))
    return

rotas_publicas=['login.login', 'login.inicial']


