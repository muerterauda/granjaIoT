from mongo.mongo_manager import estados_com_beb


def cambiar_estado(com, beb):
    estados_com_beb.replace_one({}, {"comedero_abierto": com, "bebedero_abierto": beb})
    pass


def get_estado():
    return estados_com_beb.find_one()
