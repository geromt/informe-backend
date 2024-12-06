from sqlalchemy import select, or_

from Models.autoreslibros import Autoreslibros
from Models.autoresrevistas import Autoresrevistas
from Models.participantesproyectos import Participantesproyectos
from Models.patentes import Patentes
from Models.clasificationespatentes import Clasificacionespatentes
from Models.inventorespatentesidentificador import Inventorespatentesidentificador
from Models.revistas import Revistas
from Models.libros import Libros
from Models.proyectos import Proyectos


class InformeRepository:
    def get_deserialize_documents(self, db, from_date, to_date, data_key, page=0, sex=None, title=None):
        stmt = select(
            Libros.Identificador,
            Libros.ObraTitulo,
            Libros.ObraEditorial,
            Libros.Titulo,
            Libros.AccesoElectronico,
            Libros.FechaPublicacion
        )
        if sex == "M" or sex == "F":
            sex_filter = "Masculino" if sex == "M" else "Femenino"
            stmt = stmt.filter(
                Libros.Identificador == Autoreslibros.RefPublicacion
            ).filter(
                Autoreslibros.Genero == sex_filter
            )
        if title:
            stmt = stmt.filter(Libros.Titulo.like(f"%{title}%"))
        stmt = stmt.filter(Libros.FechaPublicacion >= from_date).filter(Libros.FechaPublicacion <= to_date)

        if "wos" in data_key:
            stmt = stmt.filter(Libros.WosId != None)
        if "scotus" in data_key:
            stmt = stmt.filter(Libros.ScopusId != None)
        if data_key == "pubmed":
            stmt = stmt.filter(Libros.PubmedId != None)

        stmt = stmt.limit(100).offset(page * 100)
        with db.engine.connect() as conn:
            return conn.execute(stmt)

    def get_deserialize_articles(self, db, from_date, to_date, data_key, page=0, sex=None, title=None):
        stmt = select(
            Revistas.Identificador,
            Revistas.RevistaTitulo,
            Revistas.RevistaEditorial,
            Revistas.Titulo,
            Revistas.AccesoElectronico,
            Revistas.FechaPublicacion
        )
        if sex == "M" or sex == "F":
            sex_filter = "Masculino" if sex == "M" else "Femenino"
            stmt = stmt.filter(
                Revistas.Identificador == Autoresrevistas.RefPublicacion
            ).filter(
                Autoresrevistas.Genero == sex_filter
            )
        if title:
            stmt = stmt.filter(Revistas.Titulo.like(f"%{title}%"))
        stmt = stmt.filter(Revistas.FechaPublicacion >= from_date).filter(Revistas.FechaPublicacion <= to_date)

        if "wos" in data_key:
            stmt = stmt.filter(Revistas.WosId != None)
        if "scotus" in data_key:
            stmt = stmt.filter(Revistas.ScopusId != None)
        if data_key == "pubmed":
            stmt = stmt.filter(Revistas.PubMedId != None)

        stmt = stmt.limit(100).offset(page * 100)
        with db.engine.connect() as conn:
            return conn.execute(stmt)

    def get_deserialize_isbn(self, db, from_date, to_date, data_key="isbn", page=0, sex=None, title=None):
        stmt = select(
            Libros.Identificador,
            Libros.ObraTitulo,
            Libros.ObraEditorial,
            Libros.Titulo,
            Libros.AccesoElectronico,
            Libros.FechaPublicacion
        )
        if sex == "M" or sex == "F":
            sex_filter = "Masculino" if sex == "M" else "Femenino"
            stmt = stmt.filter(
                Libros.Identificador == Autoreslibros.RefPublicacion
            ).filter(
                Autoreslibros.Genero == sex_filter
            )
        if title:
            stmt = stmt.filter(Libros.Titulo.like(f"%{title}%"))
        stmt = stmt.filter(Libros.FechaPublicacion >= from_date).filter(Libros.FechaPublicacion <= to_date)

        stmt = stmt.filter(Libros.ObraIsbn != None)
        if data_key == "participaciones_isbn" and (sex != "M" and sex != "F"):
            stmt = stmt.filter(Libros.Identificador == Autoreslibros.RefPublicacion)

        stmt = stmt.limit(100).offset(page * 100)
        with db.engine.connect() as conn:
            return conn.execute(stmt)

    def get_deserialize_humanindex(self, db, from_date, to_date, data_key="isbn", page=0, sex=None, title=None):
        stmt = select(
            Libros.Identificador,
            Libros.ObraTitulo,
            Libros.ObraEditorial,
            Libros.Titulo,
            Libros.AccesoElectronico,
            Libros.FechaPublicacion
        )
        if sex == "M" or sex == "F":
            sex_filter = "Masculino" if sex == "M" else "Femenino"
            stmt = stmt.filter(
                Libros.Identificador == Autoreslibros.RefPublicacion
            ).filter(
                Autoreslibros.Genero == sex_filter
            )
        if title:
            stmt = stmt.filter(Libros.Titulo.like(f"%{title}%"))
        stmt = stmt.filter(Libros.FechaPublicacion >= from_date).filter(Libros.FechaPublicacion <= to_date)

        print(data_key)
        if "Libro" == data_key:
            stmt = stmt.filter(Libros.Alcance == "Libro Completo")
        elif data_key == "Capitulo":
            stmt = stmt.filter(Libros.Alcance == "Capítulo de un Libro")
        elif data_key == "Total":
            stmt = stmt.filter(or_(Libros.Alcance == "Libro Completo", Libros.Alcance == "Capítulo de un Libro"))
        elif data_key == "ParticipacionesCapitulos":
            if sex != "M" and sex != "F":
                stmt = stmt.filter(Libros.Identificador == Autoreslibros.RefPublicacion)
            stmt = stmt.filter(Libros.Alcance == "Capítulo de un Libro")
        elif data_key == "ParticipacionesLibros":
            if sex != "M" and sex != "F":
                stmt = stmt.filter(Libros.Identificador == Autoreslibros.RefPublicacion)
            stmt = stmt.filter(Libros.Alcance == "Libro Completo")

        stmt = stmt.limit(100).offset(page * 100)
        print(stmt)
        with db.engine.connect() as conn:
            return conn.execute(stmt)

    def get_revistas(self, db, sex):
        if sex == "M" or sex == "F":
            sex_filter = "Masculino" if sex == "M" else "Femenino"
            stmt = select(
                Revistas
            ).filter(
                Revistas.Identificador == Autoresrevistas.RefPublicacion
            ).filter(
                Autoresrevistas.Genero == sex_filter
            )
        else:
            stmt = select(Revistas)
        with db.engine.connect() as conn:
            return conn.execute(stmt)

    def get_libros(self, db, sex):
        if sex == "M" or sex == "F":
            sex_filter = "Masculino" if sex == "M" else "Femenino"
            stmt = select(
                Libros.Identificador,
                Libros.WosId,
                Libros.PubmedId,
                Libros.ScopusId,
                Libros.FechaPublicacion
            ).filter(
                Libros.Identificador == Autoreslibros.RefPublicacion
            ).filter(
                Autoreslibros.Genero == sex_filter
            )
        else:
            stmt = select(
                Libros.Identificador,
                Libros.WosId,
                Libros.PubmedId,
                Libros.ScopusId,
                Libros.FechaPublicacion)
        with db.engine.connect() as conn:
            return conn.execute(stmt)

    def get_libros_counter_isbn(self, db, sex):
        if sex == "M" or sex == "F":
            sex_filter = "Masculino" if sex == "M" else "Femenino"
            stmt = select(
                Libros.Identificador,
                Libros.ObraIsbn,
                Libros.FechaPublicacion
            ).where(
                Libros.ObraIsbn != None
            ).filter(
                Libros.Identificador == Autoreslibros.RefPublicacion
            ).filter(
                Autoreslibros.Genero == sex_filter
            )
        else:
            stmt = select(Libros.Id, Libros.ObraIsbn, Libros.FechaPublicacion).where(Libros.ObraIsbn != None)
        with db.engine.connect() as conn:
            return conn.execute(stmt)

    def get_participaciones_isbn(self, db, sex):
        if sex == "M" or sex == "F":
            sex_filter = "Masculino" if sex == "M" else "Femenino"
            stmt = select(
                Libros.Identificador,
                Libros.ObraIsbn,
                Libros.FechaPublicacion
            ).where(
                Libros.ObraIsbn != None
            ).filter(
                Libros.Identificador == Autoreslibros.RefPublicacion
            ).filter(
                Autoreslibros.Genero == sex_filter
            )
        else:
            stmt = select(Libros.Id, Libros.ObraIsbn, Libros.FechaPublicacion
            ).where(
                Libros.ObraIsbn != None
            ).filter(
                Libros.Identificador == Autoreslibros.RefPublicacion
            )
        with db.engine.connect() as conn:
            return conn.execute(stmt)

    def get_proyectos(self, db, sex):
        if sex == "M" or sex == "F":
            sex_filter = "Masculino" if sex == "M" else "Femenino"
            stmt = select(
                Proyectos.Identificador,
                Proyectos.FechaInicio,
                Proyectos.FechaSituacion,
                Proyectos.Convocatoria
            ).filter(
                Proyectos.Identificador == Participantesproyectos.RefProyecto
            ).filter(
                Participantesproyectos.Genero == sex_filter
            )
        else:
            stmt = select(Proyectos.Identificador, Proyectos.FechaInicio, Proyectos.FechaSituacion, Proyectos.Convocatoria)
        with db.engine.connect() as conn:
            return conn.execute(stmt)

    def get_participaciones_proyectos(self, db, sex):
        if sex == "M" or sex == "F":
            sex_filter = "Masculino" if sex == "M" else "Femenino"
            stmt = select(
                Proyectos.Identificador,
                Proyectos.FechaInicio,
                Proyectos.FechaSituacion,
                Proyectos.Convocatoria,
                Participantesproyectos.Identificador
            ).filter(
                Proyectos.Identificador == Participantesproyectos.RefProyecto
            ).filter(
                Participantesproyectos.Genero == sex_filter
            )
        else:
            stmt = select(Proyectos.Identificador,
                          Proyectos.FechaInicio,
                          Proyectos.FechaSituacion,
                          Proyectos.Convocatoria,
                          Participantesproyectos.Identificador
            ).filter(
                Proyectos.Identificador == Participantesproyectos.RefProyecto
            )
        with db.engine.connect() as conn:
            return conn.execute(stmt)

    def get_patentes_inventors(self, db):
        stmt = select(
            Patentes.Identificador,
            Patentes.Titulo,
            Patentes.FechaConcesion,
            Inventorespatentesidentificador.RefPatente,
            Inventorespatentesidentificador.NombreCompleto,
        ).filter(
            Patentes.Identificador == Inventorespatentesidentificador.RefPatente)

        with db.engine.connect() as conn:
            return conn.execute(stmt)

    def get_patentes_clasificacion(self, db):
        stmt = select(
            Patentes.Identificador,
            Clasificacionespatentes.RefPatente,
            Clasificacionespatentes.Seccion
        ).filter(
            Patentes.Identificador == Clasificacionespatentes.RefPatente)

        with db.engine.connect() as conn:
            return conn.execute(stmt)

    def get_alcance_obras(self, db, sex):
        if sex == "M" or sex == "F":
            sex_filter = "Masculino" if sex == "M" else "Femenino"
            stmt = select(
                Libros.Identificador,
                Libros.Alcance,
                Libros.FechaPublicacion
            ).filter(
                Libros.Id == Autoreslibros.RefPublicacion
            ).filter(
                Autoreslibros.Genero == sex_filter
            )
        else:
            stmt = select(
                Libros.Identificador,
                Libros.Alcance,
                Libros.FechaPublicacion
            )

        with db.engine.connect() as conn:
            return conn.execute(stmt)

    def get_participaciones_obras(self, db, sex):
        if sex == "M" or sex == "F":
            sex_filter = "Masculino" if sex == "M" else "Femenino"
            stmt = select(
                Libros.Identificador,
                Libros.Alcance,
                Libros.FechaPublicacion,
                Autoreslibros.Identificador
            ).filter(
                Libros.Identificador == Autoreslibros.RefPublicacion
            ).filter(
                Autoreslibros.Genero == sex_filter
            )
        else:
            stmt = select(
                Libros.Identificador,
                Libros.Alcance,
                Libros.FechaPublicacion,
                Autoreslibros.Identificador
            ).filter(
                Libros.Identificador == Autoreslibros.RefPublicacion
            )

        with db.engine.connect() as conn:
            return conn.execute(stmt)
