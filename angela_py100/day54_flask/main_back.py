# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from flask import Flask
app = Flask(__name__)

import random_guess
print(random_guess.__name__)
print(__name__)

def make_bold(funct):
    def wrapper():
        text = '<b>' + funct() + '</b>'
        print('text: ', text)
        return text
    return wrapper

def make_em(funct):
    def wrapper():
        text = '<em>' + funct() + '</em>'
        print('text: ', text)
        return text
    return wrapper

@app.route("/")
def hello_world():
    # print('hello world!')
    return '<h1 style="text-align: center"> Hello, World! </h1>' \
           '<p>This is a paragraph.</p>' \
           '<img src="https://media.giphy.com/media/hvS1eKlR75hMr0l7VJ/giphy-downsized-large.gif?cid=ecf05e47h7dk9712qlycxt60wm4kvzgkti278lku24j2dqft&rid=giphy-downsized-large.gif&ct=g">'

@app.route("/bye")
@make_bold
@make_em
def bye():
    return 'Bye Adios, Ciao, Au Revoir!'


@app.route('/username/<name>/<int:number>')
def greet(name, number):
    return f'hello there {name}, you are {number} years old ! '

if __name__ == "__main__":
#    hello_world()
    app.run(debug=True)

