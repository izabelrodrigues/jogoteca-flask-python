from flask import Flask,render_template, request, redirect, session, flash, url_for
from model.domains import Game, Usuario

app = Flask(__name__)
app.secret_key = 'alura'

game1 = Game('God of War 4', 'Ação', 'PS4')
game2 = Game('Super Mario RPG', 'RPG', 'SNES')
list = [game1, game2]

usuario1 = Usuario('luan', 'Luan Marques', '1234')
usuario2 = Usuario('nico', 'Nico Steppat', '7a1')
usuario3 = Usuario('flavio', 'Flávio', 'javascript')

usuarios = { usuario1.login: usuario1, 
             usuario2.login: usuario2, 
             usuario3.login: usuario3 }

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
    if request.form['usuario'] in usuarios:
        usuario = usuarios[request.form['usuario']]
        if usuario.senha == request.form['senha']:
            session['usuario_logado'] = usuario.id
            flash(usuario.nome + ' logou com sucesso!')
            proxima_pagina = request.form['proxima']
            return redirect(proxima_pagina)
    else:
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