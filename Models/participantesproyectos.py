from flask_sqlalchemy import SQLAlchemy

from Models.proyectos import Proyectos

db = SQLAlchemy()


class Participantesproyectos(db.Model):
    Identificador = db.Column(db.Integer, primary_key=True)
    RefProyecto = db.Column(db.Integer, db.ForeignKey(Proyectos.Identificador))
    Genero = db.Column(db.String(32), nullable=True)
