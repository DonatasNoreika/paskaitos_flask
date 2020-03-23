import os
from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# import forms

basedir = os.path.abspath(os.path.dirname(__file__))
print(basedir)

app = Flask(__name__)

app.config['SECRET_KEY'] = 'dfgsfdgsdfgsdfgsdf'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,
                                                                    'data.sqlite?check_same_thread=False')
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Destytojas(db.Model):
    __tablename__ = "destytojas"
    id = db.Column(db.Integer, primary_key=True)
    vardas = db.Column("Vardas", db.String)
    paskaitos = db.relationship("Paskaita")


association_table = db.Table('paskaita_studentas', db.metadata,
                             db.Column('stundentas_id', db.Integer, db.ForeignKey('studentas.id')),
                             db.Column('paskaita_id', db.Integer, db.ForeignKey('paskaita.id'))
                             )


class Paskaita(db.Model):
    __tablename__ = "paskaita"
    id = db.Column(db.Integer, primary_key=True)
    pavadinimas = db.Column("Pavadinimas", db.String)
    destytojas_id = db.Column(db.Integer, db.ForeignKey("destytojas.id"))
    destytojas = db.relationship("Destytojas")
    studentai = db.relationship("Studentas", secondary=association_table, back_populates="studentai")


class Studentas(db.Model):
    __tablename__ = "studentas"
    id = db.Column(db.Integer, primary_key=True)
    vardas = db.Column("Vardas", db.String)
    paskaitos = db.relationship("Paskaita", secondary=association_table, back_populates="paskaitos")


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
    db.create_all()
