from mongo.entity.granja import Medicion
from mongo.mongo_manager import granja_colection


def insert(m: Medicion):
    granja_colection.insert(m.get_dict_to_mongo())


def get_last(i: int = 1):
    medidas = granja_colection.find(sort=[("fecha", -1)]).limit(i)
    m = []
    for x in medidas:
        m.append(Medicion.generar_medida(x))
    return m
