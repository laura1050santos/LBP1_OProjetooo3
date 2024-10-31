class Usuario:
    def __init__(self,id, nome, senha):
        self.id= id
        self.nome = nome
        self.senha = senha

lista_usuarios=[]

lista_usuarios.append(user= Usuario('1', "igor", "1234"))
lista_usuarios.append(admin=Usuario('2', "admin", "admin"))