from flask import Blueprint, request, Response
from mongo.repository.medicion_repository import insert as insert_medicion
from mongo.entity.granja import Medicion
from datetime import datetime
import pytz as tz

granja_bp = Blueprint('medidores_granja', __name__, template_folder='templates')
zona_horaria = tz.timezone("Europe/Madrid")


@granja_bp.route("/envioParametros", methods=['GET'])
def envio_parametros():
    try:
        temperatura = float(request.args.get("temperatura"))
        humedad = float(request.args.get("humedad"))
        comida_p = float(request.args.get("comida"))
        agua_p = float(request.args.get("agua"))
        animales = float(request.args.get("animales"))
        now = datetime.now(zona_horaria)
        print(now)
        m = Medicion(temperatura, humedad, comida_p, agua_p, animales, now)
        insert_medicion(m)
        Response(status=200)
        return Response(status=200)
    except Exception as e:
        print(e)
        return Response(status=500)
