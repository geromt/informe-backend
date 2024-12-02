from sqlalchemy import select

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
                Libros.Id,
                Libros.WosId,
                Libros.PubmedId,
                Libros.ScopusId,
                Libros.FechaPublicacion
            ).filter(
                Libros.Id == Autoreslibros.RefLibro
            ).filter(
                Autoreslibros.Genero == sex_filter
            )
        else:
            stmt = select(
                Libros.Id,
                Libros.WosId,
                Libros.PubmedId,
                Libros.ScopusId,
                Libros.FechaPublicacion)
        print(stmt)
        with db.engine.connect() as conn:
            return conn.execute(stmt)

    def get_libros_counter_isbn(self, db, sex):
        if sex == "M" or sex == "F":
            sex_filter = "Masculino" if sex == "M" else "Femenino"
            stmt = select(
                Libros.Id,
                Libros.ObraIsbn,
                Libros.FechaPublicacion
            ).where(
                Libros.ObraIsbn != None
            ).filter(
                Libros.Id == Autoreslibros.RefLibro
            ).filter(
                Autoreslibros.Genero == sex_filter
            )
        else:
            stmt = select(Libros.Id, Libros.ObraIsbn, Libros.FechaPublicacion).where(Libros.ObraIsbn != None)
        print(stmt)
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
        print(stmt)
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
                Libros.Id,
                Libros.Alcance,
                Libros.FechaPublicacion
            ).filter(
                Libros.Id == Autoreslibros.RefLibro
            ).filter(
                Autoreslibros.Genero == sex_filter
            )
        else:
            stmt = select(
                Libros.Id,
                Libros.Alcance,
                Libros.FechaPublicacion
            )

        with db.engine.connect() as conn:
            return conn.execute(stmt)

    def get_participaciones_obras(self, db, sex):
        if sex == "M" or sex == "F":
            sex_filter = "Masculino" if sex == "M" else "Femenino"
            stmt = select(
                Libros.Id,
                Libros.Alcance,
                Libros.FechaPublicacion,
                Autoreslibros.Identificador
            ).filter(
                Libros.Id == Autoreslibros.RefLibro
            ).filter(
                Autoreslibros.Genero == sex_filter
            )
        else:
            stmt = select(
                Libros.Id,
                Libros.Alcance,
                Libros.FechaPublicacion,
                Autoreslibros.Identificador
            ).filter(
                Libros.Id == Autoreslibros.RefLibro
            )

        with db.engine.connect() as conn:
            return conn.execute(stmt)
