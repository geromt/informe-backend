from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from services.informe_service import InformeService
from validators.informe_validator import validate_sex
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:root@localhost/informemedicina"
db = SQLAlchemy(app)
informe_service = InformeService()


@app.route("/deserialize/<data_type>/<time_lapse>/<time>/<data_key>/<page>")
@cross_origin()
def get_deserialize(data_type, time_lapse, time, data_key, page):
    args = request.args.to_dict()
    sex = validate_sex(args)
    if not sex:
        return "Sexo no válido", 400

    print(sex)
    title = args["titulo"] if "titulo" in args else None

    if data_type == "documents":
        result = informe_service.get_deserialize_document(db, time_lapse, time, data_key, int(page), sex, title)
    elif data_type == "articles":
        result = informe_service.get_deserialize_articles(db, time_lapse, time, data_key, int(page), sex, title)
    elif data_type == "isbn":
        result = informe_service.get_deserialize_isbn(db, time_lapse, time, data_key, int(page), sex, title)
    elif data_type == "humanindex":
        result = informe_service.get_deserialize_humanindex(db, time_lapse, time, data_key, int(page), sex, title)

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
