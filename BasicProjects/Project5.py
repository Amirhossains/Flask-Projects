
from flask import Flask, redirect, url_for, render_template, request, session, flash
from time import sleep
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class Users(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    email = db.Column(db.String(100))
    password = db.Column(db.String(100))



if __name__ == '__main__':
    # db.create_all()
    app.run(debug=True)