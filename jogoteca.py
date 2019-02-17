from flask import Flask,render_template
app = Flask(__name__)

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
def lista():
    lista = getGames()
    return render_template('lista.html', title='Jogos', games=lista)
