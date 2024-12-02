from flask_sqlalchemy import SQLAlchemy

from Models.revistas import Revistas

db = SQLAlchemy()


class Autoresrevistas(db.Model):
    Identificador = db.Column(db.Integer, primary_key=True)
    RefPublicacion = db.Column(db.Integer, db.ForeignKey(Revistas.Identificador))
    Genero = db.Column(db.String(32), nullable=True)