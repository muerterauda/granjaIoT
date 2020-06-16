import json

import pytz as tz

zona_horaria = tz.timezone("Europe/Madrid")


class Medicion:

    def __init__(self, temperatura, humedad, comida, agua, animales, fecha):
        self.temperatura = temperatura
        self.humedad = humedad
        self.comida = comida
        self.agua = agua
        self.animales = animales
        self.__fecha = fecha

    @property
    def fecha(self):
        return self.__fecha.replace(tzinfo=tz.timezone('UTC')).astimezone(zona_horaria).strftime("%d/%m/%Y, %H:%M:%S")

    def get_dict(self):
        return {"temperatura": self.temperatura, "humedad": self.humedad, "agua": self.agua,
                "comida": self.comida, "animales": self.animales, "fecha": self.fecha}

    def serialize(self):
        return json.dumps(self.get_dict())

    @staticmethod
    def serialize_all(med):
        x = []
        for m in med:
            x.append(m.get_dict())
        return json.dumps(x)

    @staticmethod
    def generar_medida(med):
        return Medicion(temperatura=med.get("temperatura"), humedad=med.get("humedad"), comida=med.get("comida"),
                        agua=med.get("agua"), animales=med.get("animales"), fecha=med.get("fecha"))
