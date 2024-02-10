from flask import Flask, redirect, url_for,\
    render_template, session, request, flash
from datetime import timedelta
# from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config['SECRET_KEY'] = 'Eminem'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.permanent_session_lifetime = timedelta(minutes=10)

# db = SQLAlchemy(app)

# class users(db.Model):
#     _id = db.Column('id', db.Integer, primary_key=True)
#     name = db.Column('name', db.String(100))
#     email = db.Column('email', db.String(100))

#     def __init__(self, name, email):
#         self.name = name
#         self.email = email


@app.route('/')
def nothing():
    return redirect('/firstLogin')

@app.route('/firstLogin', methods=['GET', 'POST'])
def firstLogin():
    if request.method == 'POST':
        session.permanent = True
        session['user'] = request.form['nm']+request.form['lnm']
        if session['user'] == '':
            del session['user']
            flash('you did not enter username.')
            return render_template('ForProject4/firstLogin.html')
        else:
            # username = session['user']
            # foundUser = users.query.filter_by(name=username).first()
            # if foundUser is None:
            return redirect(url_for('secondLogin'))
            # else:
                # return redirect(url_for('user'))
    elif 'user' in session and 'email' in session:
        flash('you are already logedin.')
        return redirect(url_for('user'))
    else:
        return render_template('ForProject4/firstLogin.html')

@app.route('/secondLogin', methods=['GET', 'POST'])
def secondLogin():
    if request.method == 'POST':
        session.permanent = True
        session['email'] = request.form['eml']
        if session['email'] == '':
            del session['email']
            flash('you did not enter email.')
            return render_template('ForProject4/secondLogin.html')
        else:
            # eml = users(session['user'], session['email'])
            # db.session.add(eml)
            # db.session.commit()
            return redirect(url_for('user'))
    elif 'user' in session:
        return render_template('ForProject4/secondLogin.html')
    else:
        flash('At first you must enter your username.')
        return redirect(url_for('firstLogin'))

@app.route('/user')
def user():
    return render_template('ForProject4/user.html', user=session['user'], email=session['email'])

if __name__ == '__main__':
    # db.create_all()
    app.run(debug=True)
