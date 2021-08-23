from flask import Flask
import math
import random

random_num = math.floor(random.randint(0, 9))
print('random num: ', random_num)

app = Flask(__name__)

@app.route("/")
def prompt():
    return "guess a num by /number "

@app.route("/<int:number>")
def guess_num(number):
    if number >= 10:
        return "<h1>Please enter number 1 to 9 thanks</h1>" \
               "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'></img>"
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
