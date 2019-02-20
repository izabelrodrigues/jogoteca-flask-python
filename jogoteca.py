from flask import Flask,render_template, request, redirect, session, flash, url_for

app = Flask(__name__)
app.secret_key = 'alura'

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
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('novo')))
    return render_template('games/novo.html', title='Cadastrar Jogo')

@app.route('/add-game', methods=['POST',])
def create():
    name = request.form['nome']
    company = request.form['empresa']
    
    game = Game(name,company)
    list.append(game)

    return redirect(url_for('index'))

## Autentication Routes

@app.route('/autenticar', methods=['POST',])
def autenticar():
    if 'mestra' == request.form['senha']:
        session ['usuario_logado'] = request.form['usuario']
        flash(request.form['usuario'] + ' logou com sucesso!')
        proxima_pagina =  request.form['proxima']
        return redirect(proxima_pagina)
    else :
        flash('Não logado, tente de novo!')
        return redirect(url_for('login'))

@app.route('/login')
def login():
    paginaDestino = request.args.get('proxima')
    return render_template('login.html', title='Login', proxima=paginaDestino)

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Nenhum usuário logado!')
    return redirect(url_for('index'))