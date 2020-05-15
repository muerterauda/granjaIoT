from flask_login import UserMixin


class User(UserMixin):

    def __init__(self, diccionario):
        self.__id_mongo = diccionario.get('_id')
        if self.__id_mongo:
            self.__id_mongo = str(self.__id_mongo)
        self.id = diccionario.get('id')
        self.name = diccionario.get('name')
        self.avatar = diccionario.get('avatar')

    def user_to_dict(self) -> dict:
        return {"id": self.id, "name": self.name, "avatar": self.avatar}

    @property
    def id_mongo(self):
        return self.__id_mongo

    @property
    def id_mongo_str(self):
        return str(self.__id_mongo)

    @property
    def nombre_email(self):
        return self.id.split('@')[0]

    def __str__(self):
        return self.id + ", " + self.name
