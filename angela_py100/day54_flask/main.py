from flask import Flask, render_template
import requests

app = Flask(__name__)

url = "https://api.npoint.io/ed99320662742443cc5b"
response = requests.get(url)
print("response: ", response)
posts = response.json()
print("posts: ", posts)

# posts = ""
@app.route('/')
def home():
    return render_template("index.html", posts=posts)


@app.route('/blog/<num>')
def get_post(num):

    idx = int(num) - 1
    requested_post = None
    for post in posts:
        print("num: ", num, ", type: ", type(num), ", post id: ", post["id"], ", post id type: ", type(post["id"]) )
        if str(post["id"]) == str(num):
            requested_post = post
            print("requested_post: ", requested_post)
    print("idx: ", idx, ", posts: ", posts, "\n, requested_post: ", requested_post)
    return render_template("post.html", num=num, post=requested_post)

if __name__ == "__main__":
    app.run(debug=True)
