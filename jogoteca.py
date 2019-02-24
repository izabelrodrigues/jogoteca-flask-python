from flask import Flask,render_template, request, redirect, session, flash, url_for
from model.domains import Game, Usuario
from flask_mysqldb import MySQLdb
from dao import JogoDao, UsuarioDao

app = Flask(__name__)
app.secret_key = 'alura'
db = MySQLdb.connect(user='root', passwd='sua_senha', host='127.0.0.1', port=3306, database='jogoteca')
jogo_dao = JogoDao(db)
usuario_dao = UsuarioDao(db)

@app.route("/")
def index():
    list = jogo_dao.listar()
    return render_template('games/lista.html', title='  Jogos  ', games=list)

@app.route("/new-game")
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('novo')))
    return render_template('games/novo.html', title='Cadastrar Jogo')

@app.route('/add-game', methods=['POST',])
def create():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    
    game = Game(nome,categoria,console)
    jogo_dao.salvar(game)

    return redirect(url_for('index'))

## Autentication Routes

@app.route('/autenticar', methods=['POST',])
def autenticar():
    usuario = usuario_dao.buscar_por_id(request.form['usuario'])
    if usuario:
        if usuario.senha == request.form['senha']:
            session['usuario_logado'] = usuario.login
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