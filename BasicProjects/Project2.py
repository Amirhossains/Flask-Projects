from flask import Flask, redirect, url_for, render_template,\
request, session
from datetime import timedelta

app = Flask(__name__)
app = Flask(__name__, template_folder='templates')
app.config['SECRET_KEY'] = 'eminem'
app.permanent_session_lifetime = timedelta(days=10, minutes=2)

@app.route('/dea')
def firstUrl():
    return "<h1>HeheHaha</h1>"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'user' in session:
        return redirect(url_for("users"))
    elif request.method == 'POST':
        session.permanent = True
        session['user'] = request.form["nm"]+request.form['lnm']
        return redirect(url_for("users"))
    else:
        return render_template("Login.html")

@app.route(f'/user')
def users():
    if 'user' in session:
        return f"This is {session['user']}'s profile."
    else:
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    del session['user']
    return redirect(url_for("login"))

@app.route('/')
def nothing():
    return redirect(url_for("firstUrl"))

if __name__ == '__main__':
    app.debug=True
    app.run()