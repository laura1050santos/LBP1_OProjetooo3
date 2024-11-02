class Usuario:
    def __init__(self,id, nome, senha):
        self.id= id
        self.nome = nome
        self.senha = senha

lista_usuarios=[]
user= Usuario(1, "igor", "1234")
admin= Usuario(2, "user", "4321")
lista_usuarios.append(user)
lista_usuarios.append(admin)