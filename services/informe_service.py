import math

from DTOs.documents import DocumentsDTO
from DTOs.articles import ArticlesDTO
from DTOs.isbns import ISBNsDTO
from DTOs.patentsDTO import PatentsDTO
from DTOs.projectDTO import ProjectsDTO
from repositories.informe_repository import InformeRepository


class InformeService:
    def __init__(self):
        self.informe_repository = InformeRepository()

    def get_articles_by_year(self, db, sex="ambos"):
        articles = self._get_articles(db, lambda date: date.year, sex)
        articles.time_lapse = "year"
        return articles

    def get_articles_by_month(self, db, sex="ambos"):
        articles = self._get_articles(db, lambda date: f"{date.year}-{date.month:02d}", sex)
        articles.time_lapse = "month"
        return articles

    def get_documents_by_year(self, db, sex="ambos"):
        documents = self._get_documents(db, lambda date: date.year, sex)
        documents.time_lapse = "year"
        return documents

    def get_documents_by_month(self, db, sex="ambos"):
        documents = self._get_documents(db, lambda date: f"{date.year}-{date.month:02d}", sex)
        documents.time_lapse = "month"
        return documents

    def get_documents_with_isbn_by_year(self, db, sex="ambos"):
        isbns = self._get_documents_with_isbn(db, lambda date: date.year, sex)
        isbns.time_lapse = "year"
        return isbns

    def get_documents_with_isbn_by_month(self, db, sex="ambos"):
        isbns = self._get_documents_with_isbn(db, lambda date: f"{date.year}-{date.month:02d}", sex)
        isbns.time_lapse = "month"
        return isbns

    def get_proyectos(self, db, sex="ambos"):
        data = {}
        keys = ["Total"]
        bar_keys = []
        min_year = math.inf
        max_year = -math.inf

        for i, start_date, situation_date, conv in self.informe_repository.get_proyectos(db, sex):
            year = situation_date.year
            key = year
            adding_flag = False
            self._add_to_counter(key, data, "Total")

            if "UNAM" in conv or "unam" in conv:
                self._add_to_counter(key, data, "UNAM")
                adding_flag = True
                if "UNAM" not in bar_keys:
                    bar_keys.append("UNAM")
            if "CONACYT" in conv or "conacyt" in conv:
                self._add_to_counter(key, data, "CONACYT")
                adding_flag = True
                if "CONACYT" not in bar_keys:
                    bar_keys.append("CONACYT")
            if "PAPIME" in conv:
                self._add_to_counter(key, data, "PAPIME")
                adding_flag = True
                if "PAPIME" not in bar_keys:
                    bar_keys.append("PAPIME")
            if "PAPIIT" in conv:
                self._add_to_counter(key, data, "PAPIIT")
                adding_flag = True
                if "PAPIIT" not in bar_keys:
                    bar_keys.append("PAPIIT")
            if "propios" in conv:
                self._add_to_counter(key, data, "propios")
                adding_flag = True
                if "propios" not in bar_keys:
                    bar_keys.append("propios")
            if "Sector Público" in conv:
                self._add_to_counter(key, data, "Sector Público")
                adding_flag = True
                if "Sector Público" not in bar_keys:
                    bar_keys.append("Sector Público")
            if "Sector Privado" in conv:
                self._add_to_counter(key, data, "Sector Privado")
                adding_flag = True
                if "Sector Privado" not in bar_keys:
                    bar_keys.append("Sector Privado")

            if adding_flag:
                if year < min_year:
                    min_year = year
                if year > max_year:
                    max_year = year

        data_list = [v for k, v in data.items()]
        data_list.sort(key=lambda d: d["name"])
        print(data.values())
        bar_keys.sort(key=lambda k: sum([d[k] for d in data.values() if k in d]))
        bar_keys.reverse()

        projects = ProjectsDTO(
            from_year=min_year,
            to_year=max_year,
            data=data_list,
            keys=keys,
            bar_keys=bar_keys
        )

        return projects

    def get_patentes(self, db):
        data = {}
        min_year = math.inf
        max_year = -math.inf

        for i, titulo, date, _, Nombre in self.informe_repository.get_patentes_inventors(db):
            year = date.year
            if year < min_year:
                min_year = year
            if year > max_year:
                max_year = year

            if i in data:
                data[i]["Inventores"].append(Nombre)
            else:
                data[i] = {
                    "Id": i,
                    "Titulo": titulo,
                    "Fecha": date.year,
                    "Inventores": [Nombre],
                    "Seccion": []
                }

        for i, _, seccion in self.informe_repository.get_patentes_clasificacion(db):
            if i not in data:
                continue
            if seccion not in data[i]["Seccion"]:
                data[i]["Seccion"].append(seccion)

        data_list = [v for k, v in data.items()]
        data_list.sort(key=lambda d: d["Id"])

        patents = PatentsDTO(
            from_year=min_year,
            to_year=max_year,
            data=data_list,
        )

        return patents

    def get_humanindex(self, db, sex):
        data = {}
        keys = []
        min_year = math.inf
        max_year = -math.inf

    def _get_documents_with_isbn(self, db, name_gen, sex):
        data = {}
        keys = ["isbn"]
        min_year = math.inf
        max_year = -math.inf

        for i, isbn, date in self.informe_repository.get_libros_counter_isbn(db, sex):
            year = date.year
            if year < min_year:
                min_year = year
            if year > max_year:
                max_year = year

            key = name_gen(date)
            self._add_to_counter(key, data, "isbn")

        data_list = [v for k, v in data.items()]
        data_list.sort(key=lambda d: d["name"])
        keys.sort(key=lambda k: sum([d[k] for d in data.values() if k in d]))
        keys.reverse()

        isbns = ISBNsDTO(
            from_year=min_year,
            to_year=max_year,
            time_lapse="",
            data=data_list,
            keys=keys
        )

        return isbns

    def _get_articles(self, db, name_gen, sex):
        data = {}
        keys = []
        min_year = math.inf
        max_year = -math.inf

        for i, wos, pubmed, scotus, date in self.informe_repository.get_revistas(db, sex):
            year = date.year
            if year < min_year:
                min_year = year
            if year > max_year:
                max_year = year

            key = name_gen(date)

            if wos:
                self._add_to_counter(key, data, "wos")
                if "wos" not in keys:
                    keys.append("wos")
            if pubmed:
                self._add_to_counter(key, data, "pubmed")
                if "pubmed" not in keys:
                    keys.append("pubmed")
            if scotus:
                self._add_to_counter(key, data, "scotus")
                if "scotus" not in keys:
                    keys.append("scotus")
            if scotus and wos:
                self._add_to_counter(key, data, "wos_scotus")
                if "wos_scotus" not in keys:
                    keys.append("wos_scotus")

        data_list = [v for k, v in data.items()]
        data_list.sort(key=lambda d: d["name"])
        keys.sort(key=lambda k: sum([d[k] for d in data.values() if k in d]))
        keys.reverse()

        articles = ArticlesDTO(
            from_year=min_year,
            to_year=max_year,
            time_lapse="",
            data=data_list,
            keys=keys
        )
        return articles

    def _get_documents(self, db, name_gen, sex):
        data = {}
        keys = []
        min_year = math.inf
        max_year = -math.inf

        for i, wos, pubmed, scotus, date in self.informe_repository.get_libros(db, sex):
            key = name_gen(date)
            added_flag = False

            if wos:
                self._add_to_counter(key, data, "wos")
                added_flag = True
                if "wos" not in keys:
                    keys.append("wos")
            if pubmed:
                self._add_to_counter(key, data, "pubmed")
                added_flag = True
                if "pubmed" not in keys:
                    keys.append("pubmed")
            if scotus:
                self._add_to_counter(key, data, "scotus")
                added_flag = True
                if "scotus" not in keys:
                    keys.append("scotus")
            if scotus and wos:
                self._add_to_counter(key, data, "wos_scotus")
                added_flag = True
                if "wos_scotus" not in keys:
                    keys.append("wos_scotus")

            if added_flag:
                year = date.year
                if year < min_year:
                    min_year = year
                if year > max_year:
                    max_year = year

        data_list = [v for k, v in data.items()]
        data_list.sort(key=lambda d: d["name"])
        keys.sort(key=lambda k: sum([d[k] for d in data.values() if k in d]))
        keys.reverse()

        documents = DocumentsDTO(
            from_year=min_year,
            to_year=max_year,
            time_lapse="",
            data=data_list,
            keys=keys
        )
        return documents

    def _add_to_counter(self, name, data, data_key):
        if name in data:
            if data_key in data[name]:
                data[name][data_key] += 1
            else:
                data[name][data_key] = 1
        else:
            data[name] = {"name": name}
