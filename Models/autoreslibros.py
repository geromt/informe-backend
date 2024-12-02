from flask_sqlalchemy import SQLAlchemy

from Models.libros import Libros

db = SQLAlchemy()


class Autoreslibros(db.Model):
    Identificador = db.Column(db.Integer, primary_key=True)
    RefLibro = db.Column(db.Integer, db.ForeignKey(Libros.Id))
    Genero = db.Column(db.String(32), nullable=True)