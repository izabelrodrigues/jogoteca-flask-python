from flask import Flask,render_template, request, redirect
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

class Game:
    def __init__(self, name, company):
        self.name = name
        self.company = company

game1 = Game('March of Empires', 'Gameloft')
game2 = Game('Canddy Crush', 'King')
list = [game1, game2]

@app.route("/")
def index():
    return render_template('lista.html', title='  Jogos  ', games=list)

@app.route("/new-game")
def novo():
    return render_template('novo.html', title='Novo Jogo')

@app.route('/add-game', methods=['POST',])
def create():
    name = request.form['nome']
    company = request.form['empresa']
    
    game = Game(name,company)
    list.append(game)

    return redirect('/')
