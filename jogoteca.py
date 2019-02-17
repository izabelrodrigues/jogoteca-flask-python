from flask import Flask,render_template
app = Flask(__name__)

@app.route("/")
def lista():
    lista = ['Tetris','March of Empires', 'Candy Crush']
    return render_template('lista.html', title='Jogos', games=lista)
