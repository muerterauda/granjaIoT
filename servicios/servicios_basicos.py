from flask import Blueprint, request

granja_bp = Blueprint('medidores_granja', __name__, template_folder='templates')


@granja_bp.route("/prueba", methods=['GET'])
def metodo_prueba():
    dato = request.args.get("dato")
    return "Si"
