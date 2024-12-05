from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from services.informe_service import InformeService
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:root@localhost/informemedicina"
db = SQLAlchemy(app)
informe_service = InformeService()


@app.route("/deserialize/documents/<datakey>/<page>")
@cross_origin()
def get_deserialize_documents(datakey, page):
    args = request.args.to_dict()
    sex = "ambos"
    if "sexo" in args:
        sex = args["sexo"]
        if sex != "M" and sex != "F":
            return "Sexo no válido", 400
    result = informe_service.get_deserialize_document(db, sex, datakey, int(page))
    return jsonify(result.to_dict()), 200

@app.route("/documents/year/", methods=["GET"])
@cross_origin()
def get_documents_by_year():
    args = request.args.to_dict()
    sex = "ambos"
    if "sexo" in args:
        sex = args["sexo"]
        if sex != "M" and sex != "F":
            return "Sexo no válido", 400
    result = informe_service.get_documents_by_year(db, sex)
    return jsonify(result.to_dict()), 200


@app.route("/documents/month/", methods=["GET"])
@cross_origin()
def get_documents_by_month():
    args = request.args.to_dict()
    sex = "ambos"
    if "sexo" in args:
        sex = args["sexo"]
        if sex != "M" and sex != "F":
            return "Sexo no válido", 400
    result = informe_service.get_documents_by_month(db, sex)
    return jsonify(result.to_dict()), 200


@app.route("/articles/year/", methods=["GET"])
@cross_origin()
def get_articles_by_year():
    args = request.args.to_dict()
    sex = "ambos"
    if "sexo" in args:
        sex = args["sexo"]
        if sex != "M" and sex != "F":
            return "Sexo no válido", 400
    result = informe_service.get_articles_by_year(db, sex)
    return jsonify(result.to_dict()), 200


@app.route("/articles/month/", methods=["GET"])
@cross_origin()
def get_articles_by_month():
    args = request.args.to_dict()
    sex = "ambos"
    if "sexo" in args:
        sex = args["sexo"]
        if sex != "M" and sex != "F":
            return "Sexo no válido", 400
    result = informe_service.get_articles_by_month(db, sex)
    return jsonify(result.to_dict()), 200


@app.route("/isbn/year", methods=["GET"])
@cross_origin()
def get_isbn_by_year():
    args = request.args.to_dict()
    sex = "ambos"
    if "sexo" in args:
        sex = args["sexo"]
        if sex != "M" and sex != "F":
            return "Sexo no válido", 400
    result = informe_service.get_documents_with_isbn_by_year(db, sex)
    return jsonify(result.to_dict()), 200


@app.route("/isbn/month", methods=["GET"])
@cross_origin()
def get_isbn_by_month():
    args = request.args.to_dict()
    sex = "ambos"
    if "sexo" in args:
        sex = args["sexo"]
        if sex != "M" and sex != "F":
            return "Sexo no válido", 400
    result = informe_service.get_documents_with_isbn_by_month(db, sex)
    return jsonify(result.to_dict()), 200


@app.route("/humanindex/year", methods=["GET"])
@cross_origin()
def get_humanindex_by_year():
    args = request.args.to_dict()
    sex = "ambos"
    if "sexo" in args:
        sex = args["sexo"]
        if sex != "M" and sex != "F":
            return "Sexo no válido", 400
    result = informe_service.get_humaninedx_by_year(db, sex)
    return jsonify(result.to_dict()), 200


@app.route("/humanindex/month", methods=["GET"])
@cross_origin()
def get_humanindex_by_month():
    args = request.args.to_dict()
    sex = "ambos"
    if "sexo" in args:
        sex = args["sexo"]
        if sex != "M" and sex != "F":
            return "Sexo no válido", 400
    result = informe_service.get_humanindex_by_month(db, sex)
    return jsonify(result.to_dict()), 200


@app.route("/proyectos/", methods=["GET"])
@cross_origin()
def get_projects():
    args = request.args.to_dict()
    sex = "ambos"
    if "sexo" in args:
        sex = args["sexo"]
        if sex != "M" and sex != "F":
            return "Sexo no válido", 400
    result = informe_service.get_proyectos(db, sex)
    return jsonify(result.to_dict()), 200


@app.route("/participaciones-proyectos/", methods=["GET"])
@cross_origin()
def get_participaciones_projects():
    args = request.args.to_dict()
    sex = "ambos"
    if "sexo" in args:
        sex = args["sexo"]
        if sex != "M" and sex != "F":
            return "Sexo no válido", 400
    result = informe_service.get_participaciones_proyectos(db, sex)
    return jsonify(result.to_dict()), 200


@app.route("/patentes/", methods=["GET"])
@cross_origin()
def get_patentes():
    result = informe_service.get_patentes(db)
    return jsonify(result.to_dict()), 200


if __name__ == "__main__":
    app.run(debug=True)
