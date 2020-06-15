import json


class Medicion:

    def __init__(self, temperatura, humedad, comida, agua, animales, fecha):
        self.temperatura = temperatura
        self.humedad = humedad
        self.comida = comida
        self.agua = agua
        self.animales = animales
        self.fecha = fecha

    def get_dict(self):
        return {"temperatura": self.temperatura, "humedad": self.humedad, "agua": self.agua,
                           "comida": self.comida, "animales": self.animales, "fecha": self.fecha}

    def serialize(self):
        return json.dumps(self.get_dict())
