from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Patentes(db.Model):
    Identificador = db.Column(db.Integer, primary_key=True)
    Titulo = db.Column(db.String(256), nullable=True)
    FechaConcesion = db.Column(db.Date, nullable=True)