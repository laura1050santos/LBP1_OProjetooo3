from flask import Blueprint, render_template, request, redirect, url_for, session, flash, abort, make_response
from models.usuario import lista_usuarios

loginController = Blueprint('login', __name__)

@loginController.route("/")
def inicial():
    return render_template("index.html")

@loginController.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        nome = request.form.get('nome') #usa o 'name' do input pra pegar a informação do formulario
        senha = request.form.get('senha')
        for usuario in lista_usuarios:
            if usuario.nome == nome and usuario.senha == senha: #criar a session quando o usuario acertar o login, depois da validação
                session['iduser']= usuario.id
                return redirect(url_for('login.dashboard'))
        flash("credenciais invalidas", 'error')     
        flash("tente novamente", 'info')   
    return render_template("login.html")

rotas_publicas = ["login.login", "login.index"]

@loginController.before_request #middleware (hooks)
def verificaLogin(): #pergunta se o usuario está logado (para não "gastar" processamento)
    print(1)
    if request.endpoint=='login.login' and 'iduser' in session:
        return redirect(url_for('login.index'))
    print(2)
    if request.endpoint in rotas_publicas:
        return 
    print(3)
    if "iduser" not in session: #verifica se o user ta na sessão
        return redirect(url_for('login.login'))
    print(4)
    return

@loginController.route('/dashboard')
def dashboard():
        return render_template('dash.html')  

@loginController.route('/logout')
def logout():
    response=make_response(redirect(url_for("login.login")))
    session.pop("iduser", None) 
    response.set_cookie('nome', '', expires=0)
    response.set_cookie('senha', '', expires=0)
    return response

@loginController.route("/admin")
def admin():
    if session.get("iduser") != 1:
        abort(401)
    return render_template('admin.html')

@loginController.route("/cookie")   
def cookies():
    if request.method == 'POST':
        nome = request.form['nome']
        senha = request.form['senha']
        response=make_response(render_template('fim.html')) #cia os cookies
        if nome == lista_usuarios:
            response.set_cookie('nome', 'Correto', max_age=60 * 60 *24)
        else:
            response.set_cookie('nome', 'Incorreto', max_age=60 * 60 *24)

        if senha == lista_usuarios:
            response.set_cookie('senha', 'Correto', max_age=60 * 60 *24)
        else: 
            response.set_cookie('senha', 'Incorreto', max_age=60 * 60 *24)
        return response
    return render_template('login.html')

