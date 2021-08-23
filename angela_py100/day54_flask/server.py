import requests
import random
from flask import Flask, render_template, url_for
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home(name=None):
    random_number = random.randint(1, 10)
#    curyear = datetime.now().strftime("%Y")
    curyear = datetime.now().year
    print('curyear: ', curyear)


    return render_template("helloworld.html", year=curyear, num=random_number)

@app.route("/guess/<name>")
def guess(name=None):
    print('name: ', name)
    url = f"https://api.agify.io/?name={name}"
    age = requests.get(url)
    age = age.json()["age"]
    print('url: ', url)
    print('age: ', age)

    url = f"https://api.genderize.io/?name={name}"
    gender = requests.get(url)
    gender = gender.json()["gender"]
    print('gender: ', gender)

    return render_template("guess.html", name=name.title(), age=age, gender=gender)

@app.route("/blog/<num>")
def get_blog(num):
    print("num: ", num)
    # blog_url = "https://www.npoint.io/docs/ed99320662742443cc5b"
    blog_url = "https://api.npoint.io/ed99320662742443cc5b"
    response = requests.get(blog_url)
    response = response.json()
    print(response)
    # print(response)
    posts = response
    return render_template("blog.html", posts=posts)

if __name__ == "__main__":
#    url_for('static', filename='angela.png')
    app.run(debug=True)
