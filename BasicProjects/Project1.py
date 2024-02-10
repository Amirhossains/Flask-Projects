from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/firstProject")
def home():
    return 'this is my first project of <h1>Flask</h1>'

@app.route("/DirectePage")
def Here():
    return "You were redirected to this page."

@app.route('/')
def hello():
    return redirect(url_for("Here"))

@app.route('/yoyoyo')
def nothing():
    return redirect(url_for("home"))

@app.route("/<name>")
def user(name):
    return f"<p>Hello {name} <h2>:)</h2></p>"

if __name__ == "__main__":
    app.run()