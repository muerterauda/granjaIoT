from flask import Blueprint
from flask_login import login_required

servicios_basicos_bp = Blueprint('Seguridad_servicios_basicos', __name__, template_folder='templates')


@servicios_basicos_bp.route("/fake", methods=['GET'])
@login_required
def metodo_prueba():
    return "Si"
