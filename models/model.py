lst_users = []

class Usuarios:
    def __init__(self, user,senha):
        self.user = user
        self.senha = senha



p1 = Usuarios('user',"abc123")
lst_users.append(p1)
p2 = Usuarios('admin', "adm123")
lst_users.append(p2)
