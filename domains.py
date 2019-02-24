class Game:
    def __init__(self, nome, categoria, console, id=None):
        self.id = id
        self.nome = nome
        self.categoria = categoria
        self.console = console

class Usuario:
    def __init__(self, login, nome, senha):
        self.login = login
        self.nome = nome
        self.senha = senha