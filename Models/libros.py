from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Libros(db.Model):
    Id = db.Column(db.Integer, primary_key=True)
    Alcance = db.Column(db.String(30),nullable=True)
    ObraIsbn = db.Column(db.String(20), nullable=True)
    WosId = db.Column(db.String(20), nullable=True)
    PubmedId = db.Column(db.String(20), nullable=True)
    ScopusId = db.Column(db.String(20), nullable=True)
    FechaPublicacion = db.Column(db.Date, nullable=True)