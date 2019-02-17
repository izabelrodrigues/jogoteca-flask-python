from flask import Flask,render_template, request
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

class Game:
    def __init__(self, name, company):
        self.name = name
        self.company = company

def getGames():
    game1 = Game('March of Empires', 'Gameloft')
    game2 = Game('Canddy Crush', 'King')
    list = [game1, game2]
    return list

@app.route("/")
def index():
    lista = getGames()
    return render_template('lista.html', title='  Jogos  ', games=lista)

@app.route("/new-game")
def novo():
    return render_template('novo.html', title='Novo Jogo')

@app.route('/add-game', methods=['POST',])
def create():
    lista = getGames()
    name = request.form['nome']
    company = request.form['empresa']
    
    game = Game(name,company)
    lista.append(game)

    return render_template('lista.html', title='  Jogos  ', games=lista)
