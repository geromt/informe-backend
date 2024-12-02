from flask_sqlalchemy import SQLAlchemy

from Models.patentes import Patentes

db = SQLAlchemy()


class Clasificacionespatentes(db.Model):
    Identificador = db.Column(db.Integer, primary_key=True)
    RefPatente = db.Column(db.Integer, db.ForeignKey(Patentes.Identificador))
    Seccion = db.Column(db.String(256), nullable=True)