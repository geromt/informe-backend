from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Libros(db.Model):
    Identificador = db.Column(db.Integer, primary_key=True)
    ObraTitulo = db.Column(db.Text, nullable=True)
    ObraEditorial = db.Column(db.Text, nullable=True)
    Titulo = db.Column(db.Text, nullable=True)
    AccesoElectronico = db.Column(db.Text, nullable=True)
    Alcance = db.Column(db.String(30), nullable=True)
    ObraIsbn = db.Column(db.String(20), nullable=True)
    WosId = db.Column(db.String(20), nullable=True)
    PubmedId = db.Column(db.String(20), nullable=True)
    ScopusId = db.Column(db.String(20), nullable=True)
    FechaPublicacion = db.Column(db.Date, nullable=True)