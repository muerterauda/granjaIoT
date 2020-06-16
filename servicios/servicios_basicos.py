from flask import Blueprint, request, Response
from mongo.repository.medicion_repository import insert as insert_medicion, get_last as get_last_mediciones
from mongo.entity.granja import Medicion, zona_horaria
from datetime import datetime

granja_bp = Blueprint('medidores_granja', __name__, template_folder='templates')


@granja_bp.route("/envioParametros", methods=['GET'])
def envio_parametros():
    try:
        temperatura = float(request.args.get("temperatura"))
        humedad = float(request.args.get("humedad"))
        comida_p = float(request.args.get("comida"))
        agua_p = float(request.args.get("agua"))
        animales = float(request.args.get("animales"))
        now = datetime.now(zona_horaria)
        m = Medicion(temperatura, humedad, comida_p, agua_p, animales, now)
        insert_medicion(m)
        Response(status=200)
        return Response(status=200)
    except Exception as e:
        print(e)
        return Response(status=500)


@granja_bp.route("/get_ultimas_mediciones", methods=['GET'])
def get_utlimas_mediciones():
    try:
        cantidad = int(request.args.get("cantidad"))
        if cantidad < 1:
            cantidad = 1
        m = get_last_mediciones(cantidad)
        m = Medicion.serialize_all(m)
        return m, 200
    except Exception as e:
        print(e)
        return Response(status=500)
