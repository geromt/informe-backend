from flask_sqlalchemy import SQLAlchemy

from Models.patentes import Patentes

db = SQLAlchemy()


class Inventorespatentesidentificador(db.Model):
    Identificador = db.Column(db.Integer, primary_key=True)
    RefPatente = db.Column(db.Integer, db.ForeignKey(Patentes.Identificador))
    NombreCompleto = db.Column(db.String(256), nullable=True)
    Genero = db.Column(db.String(32), nullable=True)