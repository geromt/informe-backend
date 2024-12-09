from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Proyectos(db.Model):
    Identificador = db.Column(db.Integer, primary_key=True)
    Nombre = db.Column(db.String(512), nullable=True)
    Situacion = db.Column(db.String(50), nullable=True)
    Area = db.Column(db.String(50), nullable=True)
    FechaInicio = db.Column(db.Date, nullable=True)
    FechaSituacion = db.Column(db.Date, nullable=True)
    Convocatoria = db.Column(db.String(512), nullable=True)