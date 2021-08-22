from random import Random
import math
import flask

random_num = math.floor(Random().random() * 10 )
print('random num: ', random_num)

app = flask.Flask(__name__)

@app.route("/")
def prompt():
    return "guess a num by /number "

@app.route("/<int:number>")
def guess_num(number):
    if number >= 10:
        return "<h1>Please enter number 1 to 9 thanks</h1>"
    if number < random_num:
        return "<h1 style='color:blue'>too low</h1>" \
                "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'></img>"
    elif number > random_num:
        return "<h1 style='color:blue'>too high</h1>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'></img>"
    elif number == random_num:
        return "<h1 style='color:red'>correct! </h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'></img>"


if __name__ == "__main__":
    app.run(debug=True)
