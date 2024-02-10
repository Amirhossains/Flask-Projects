from flask import Flask, redirect, url_for,\
request, session, flash, render_template
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'eminem'
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///users.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.permanent_session_lifetime = timedelta(minutes=4)

db = SQLAlchemy(app)

class users(db.Model):
    _id = db.Column('id', db.Integer, primary_key=True)
    _name = db.Column('name', db.String(150))
    _email = db.Column('email', db.String(150)) 

    def __init__(self, _name, _email):
        name = self._name
        email = self._email


@app.route('/firstPage')
def firstPage():
    return '<h1>HeheHaha</h1>'

@app.route('/')
def nothing():
    return redirect(url_for('firstPage'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'user' in session and 'email' in session:
        if session['user'] == "" or session['email'] == "":
            del session['user']
            del session['email']
            flash('You did not enter the info compeletly.')
            return render_template('loginPage.html')
        flash('You are already loged in.')
        return redirect(url_for('user'))
    elif request.method == 'POST':
        session.permanent = True
        session['user'] = request.form['nm']+request.form['lnm']
        session['email'] = request.form['eml']
        if session['user'] == "":
            flash('You did not enter your user name.')
            if session['email'] == "":
                flash('You did not enter your email.')
            del session['user']
            del session['email']
            return redirect(url_for('login'))
        if session['email'] == "":
            del session['user']
            del session['email']
            flash('You did not enter your email.')
            return redirect(url_for('login'))
        flash('You were loged in successfully.')
        return redirect(url_for('user'))
    else:
        return render_template('loginPage.html')

@app.route('/user')
def user():
    if 'user' in session or 'email' in session:
        if session['user'] == "" or session['email'] == "":
            return redirect(url_for('login'))
        name = session['user']
        email = session['email']
        return render_template('userPage.html', user=name, email=email)
    else:
        flash('You did not log in!')
        return redirect(url_for('login'))
    
@app.route('/logout')
def logout():
    if 'user' in session and 'email' in session:
        flash('You were loged out successfully.')
        del session['user']
        del session['email']
        return redirect(url_for('login'))
    else:
        flash('You are already loged out.')
        return redirect(url_for('login'))

if '__main__' == __name__:
    app.run(debug=True)
