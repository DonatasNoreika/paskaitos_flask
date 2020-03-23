from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from wtforms_sqlalchemy.fields import QuerySelectField
import app


class DestytojasForm(FlaskForm):
    vardas = StringField('Vardas', [DataRequired()])


class PaskaitaForm(FlaskForm):
    pavadinimas = StringField('Pavadinimas', [DataRequired()])


class StudentasForm(FlaskForm):
    vardas = StringField('Vardas', [DataRequired()])
