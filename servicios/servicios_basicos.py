from flask import Blueprint, request, render_template, make_response
from mongo.mongo_manager import granja_colection

granja_bp = Blueprint('medidores_granja', __name__, template_folder='templates')


@granja_bp.route("/prueba", methods=['GET'])
def metodo_prueba():
    dato = request.args.get("dato")
    granja_colection.insert({"dato": dato})
    return render_template("inicio.html")

@granja_bp.route("/prueba2", methods=['GET'])
def metodo_prueba2():
    dato = request.args.get("dato")
    granja_colection.insert({"dato": dato})
    return make_response()
