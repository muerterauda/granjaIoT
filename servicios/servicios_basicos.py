from flask import Blueprint
from flask_login import login_required

servicios_basicos_bp = Blueprint('medidores_granja', __name__, template_folder='templates')


@servicios_basicos_bp.route("/fake", methods=['GET'])
def metodo_prueba():
    return "Si"
