from flask import Flask, render_template
import requests

app = Flask(__name__)

# posts = ""
@app.route('/')
def home():
    url = "https://api.npoint.io/ed99320662742443cc5b"
    response = requests.get(url)
    print("response: ", response)
    posts = response.json()
    print("posts: ", posts)
    return render_template("index.html", posts=posts)


@app.route('/blog/<num>')
def get_post(num):
    url = "https://api.npoint.io/ed99320662742443cc5b"
    response = requests.get(url)
    # print("response: ", response)
    posts = response.json()
    idx = int(num)
    post = posts[idx - 1]
    print("idx: ", idx, ", posts: ", posts, "\n, post: ", post)
    return render_template("post.html", num=num, post=post)

if __name__ == "__main__":
    app.run(debug=True)
