from flask import Flask,render_template, request, redirect

app = Flask(__name__)

class Game:
    def __init__(self, name, company):
        self.name = name
        self.company = company

game1 = Game('March of Empires', 'Gameloft')
game2 = Game('Canddy Crush', 'King')
list = [game1, game2]

@app.route("/")
def index():
    return render_template('games/lista.html', title='  Jogos  ', games=list)

@app.route("/new-game")
def novo():
    return render_template('games/novo.html', title='Cadastrar Jogo')

@app.route('/add-game', methods=['POST',])
def create():
    name = request.form['nome']
    company = request.form['empresa']
    
    game = Game(name,company)
    list.append(game)

    return redirect('/')

## Autentication Routes

@app.route('/autenticar', methods=['POST',])
def autenticar():
    if 'mestra' == request.form['senha']:
        return redirect('/')
    else :
        return redirect ('/login')

@app.route('/login')
def login():
    return render_template('login.html', title='Login')