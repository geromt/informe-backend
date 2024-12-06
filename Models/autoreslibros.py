from flask_sqlalchemy import SQLAlchemy

from Models.libros import Libros

db = SQLAlchemy()


class Autoreslibros(db.Model):
    Identificador = db.Column(db.Integer, primary_key=True)
    RefPublicacion = db.Column(db.Integer, db.ForeignKey(Libros.Identificador))
    Genero = db.Column(db.String(32), nullable=True)