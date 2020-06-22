import json

from flask import Blueprint, request, Response
from mongo.repository.medicion_repository import insert as insert_medicion, get_last as get_last_mediciones
from mongo.repository.estado_repository import cambiar_estado, get_estado
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
        comedero = float(request.args.get("comedero"))
        bebedero = float(request.args.get("bebedero"))
        animales = float(request.args.get("animales"))
        now = datetime.now(zona_horaria)
        med = get_last_mediciones(1)
        beb_a = True
        com_a = True
        if med:
            beb_a = med[0].bebedero_abierto
            com_a = med[0].comedero_abierto
        m = Medicion(temperatura, humedad, comida_p, agua_p, animales, comedero, bebedero, com_a, beb_a, now)
        insert_medicion(m)
        r = Response(status=200)
        r.headers["Access-Control-Allow-Origin"] = "*"
        return r
    except Exception as e:
        print(e)
        return Response(status=500)


@granja_bp.route("/cambiar_estado_comedero", methods=['GET'])
def cambiar_estado_comedero():
    try:
        e = get_estado()
        com = e.get("comedero_abierto")
        beb = e.get("bebedero_abierto")
        cambiar_estado(not com, beb)
        r = Response(status=200)
        r.headers["Access-Control-Allow-Origin"] = "*"
        return r
    except Exception as e:
        print(e)
        return Response(status=500)


@granja_bp.route("/cambiar_estado_bebedero", methods=['GET'])
def cambiar_estado_bebedero():
    try:
        e = get_estado()
        com = e.get("comedero_abierto")
        beb = e.get("bebedero_abierto")
        cambiar_estado(com, not beb)
        r = Response(status=200)
        r.headers["Access-Control-Allow-Origin"] = "*"
        return r
    except Exception as e:
        print(e)
        return Response(status=500)


@granja_bp.route("/get_estado_comedero_bebedero", methods=['GET'])
def get_estado_comedero_bebero():
    try:
        e = get_estado()
        res = {"comedero_abierto": 1 if e.get("comedero_abierto") else 0,
               "bebedero_abierto": 1 if e.get("bebedero_abierto") else 0}
        r = Response(json.dumps(res), status=200)
        r.headers["Access-Control-Allow-Origin"] = "*"
        return r
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
        m = Medicion.serialize_all(m, True)
        return m, 200
    except Exception as e:
        print(e)
        return Response(status=500)
