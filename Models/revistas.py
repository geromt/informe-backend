from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Revistas(db.Model):
    Identificador = db.Column(db.Integer, primary_key=True)
    WosId = db.Column(db.String(20), nullable=True)
    PubMedId = db.Column(db.String(20), nullable=True)
    ScopusId = db.Column(db.String(20), nullable=True)
    FechaPublicacion = db.Column(db.Date, nullable=True)

    def __repr__(self):
        return f"<Id {self.Id}> <WosId {self.WosId}> <PubMedId {self.PubMedId}> <ScopusId {self.ScopusId}>"
