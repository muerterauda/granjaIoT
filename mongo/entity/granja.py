import json

import pytz as tz

zona_horaria = tz.timezone("Europe/Madrid")


class Medicion:

    def __init__(self, temperatura, humedad, comida, agua, animales, comedero, bebedero, comedero_abierto, bebedero_abierto, fecha):
        self.temperatura = temperatura
        self.humedad = humedad
        self.comida = comida
        self.agua = agua
        self.animales = animales
        self.comedero = comedero
        self.bebedero = bebedero
        self.bebedero_abierto = bebedero_abierto
        self.comedero_abierto = comedero_abierto
        self.__fecha = fecha

    @property
    def fecha(self):
        return self.__fecha.replace(tzinfo=tz.timezone('UTC')).astimezone(zona_horaria).strftime("%d/%m/%Y, %H:%M:%S")

    @property
    def fecha_reducida(self):
        return self.__fecha.replace(tzinfo=tz.timezone('UTC')).astimezone(zona_horaria).strftime("%d/%m,%H:%M")

    def get_dict_to_mongo(self):
        return {"temperatura": self.temperatura, "humedad": self.humedad, "agua": self.agua,
                "comida": self.comida, "animales": self.animales, "bebedero": self.bebedero, "comedero": self.comedero,
                "fecha": self.__fecha, "bebedero_abierto": self.bebedero_abierto,  "comedero_abierto": self.comedero_abierto}

    def get_dict(self, fecha_red=False):
        return {"temperatura": self.temperatura, "humedad": self.humedad, "agua": self.agua,
                "comida": self.comida, "animales": self.animales, "bebedero": self.bebedero,
                "comedero": self.comedero, "bebedero_abierto": self.bebedero_abierto,
                "comedero_abierto": self.comedero_abierto,
                "fecha": (self.fecha if not fecha_red else self.fecha_reducida)}

    def serialize(self, fecha_red=False):
        return json.dumps(self.get_dict(fecha_red))

    @staticmethod
    def serialize_all(med, fecha_red=False):
        x = []
        for m in med:
            x.append(m.get_dict(fecha_red))
        return json.dumps(x)

    @staticmethod
    def generar_medida(med):
        return Medicion(temperatura=med.get("temperatura"), humedad=med.get("humedad"), comida=med.get("comida"),
                        agua=med.get("agua"), animales=med.get("animales"), fecha=med.get("fecha"),
                        bebedero=med.get("bebedero"),comedero=med.get("comedero"),
                        bebedero_abierto=med.get("bebedero_abierto"), comedero_abierto=med.get("comedero_abierto"))
