from mongo.entity.granja import Medicion
from mongo.mongo_manager import granja_colection


def insert(m: Medicion):
    granja_colection.insert(m.get_dict())
