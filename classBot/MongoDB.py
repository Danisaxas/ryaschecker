import pymongo
from datetime import datetime, timedelta
import pytz
from pymongo import UpdateOne

class MondB:
    def __init__(self,
                 id: int = 0,
                 name: str = "",
                 username: str = "",
                 idchat: int = 0,
                 tipo: str = "",
                 ):
        self.id = id
        self.name = name
        self.username = username
        self.idchat = idchat
        self.tipo = tipo
        self.url = 'mongodb://mongo:AmgoVcezgoCslzqtaMYuHIjXvvdZMnlI@tramway.proxy.rlwy.net:48687'
        self._client = pymongo.MongoClient(self.url, serverSelectionTimeoutMS=5000)
        self._db = self._client['bot']
        self._key_collection = self._db['key']

    def queryUser(self):
        _collection = self._db['user']
        _consult = {"_id": self.idchat}
        return _collection.find_one(_consult)

    def savedbuser(self):
        _collection = self._db['user']
        existing_user = _collection.find_one({"_id": self.id})
        if existing_user:
            print(f"El usuario con ID {self.id} ya está registrado.")
            return False
        _save = {
            "_id": self.id,
            "username": self.username,
            "plan": "Free",
            "role": "User",
            "status": "Libre",
            "credits": 0,
            "antispam": 60,
            "time_user": 0,
            "alerts": 0,
            "since": datetime.now(),
            "key": 'None',
            "lang": "es",
            "expiracion": "0d-00h-00m-00s",  # Valor por defecto en formato string
            "dias": 0                        # Valor por defecto
        }
        _collection.insert_one(_save)
        return True

    def savepremium(self):
        _collection = self._db['user']
        myquery = {"plan": "Free"}
        newvalues = {"$set": {"plan": "premium"}}
        _collection.update_one(myquery, newvalues)

    def savedbgrup(self, dias: int = 0, plan: str = ""):
        _collection = self._db['group']
        if dias == 0:
            if plan == "":
                _save = {
                    "_id": self.idchat,
                    "days": dias,
                    "plan": 'Free Chat',
                    "type": self.tipo
                }
                return _collection.insert_one(_save)
            else:
                _save = {
                    "_id": self.idchat,
                    "days": dias,
                    "plan": 'Premium',
                    "type": self.tipo
                }
                return _collection.insert_one(_save)
        else:
            _save = {
                "_id": self.idchat,
                "days": dias,
                "plan": plan,
                "type": self.tipo
            }
            return _collection.insert_one(_save)

    def querygrup(self):
        _collection = self._db['group']
        _consult = {"id": self.idchat}
        return _collection.find_one(_consult)

    def querycora(self):
        _collection = self._db['corazon']
        _consult = {"id": self.idchat}
        return _collection.find_one(_consult)

    def savecora(self):
        _collection = self._db['corazon']
        _consult = {"id": self.idchat}
        return _collection.insert_one(_consult)

    def savelang(self):
        _collection = self._db['lang']
        _save = {
            "_id": self.id,
            "username": self.username,
            "plan": "Free",
            "role": "User",
            "status": "Libre",
            "credits": 0,
            "antispam": 60,
            "time_user": 0,
            "alerts": 0,
            "since": datetime.now(),
            "key": 'None',
            "lang": "es",
            "expiracion": "0d-00h-00m-00s",  # Igual aquí si quieres
            "dias": 0
        }
        return _collection.insert_one(_save)

    def save_generated_key(self, key: str, dias: int, usuario: str):
        venezuela = pytz.timezone("America/Caracas")
        now = datetime.now(pytz.utc).astimezone(venezuela)
        expiracion = now + timedelta(days=dias)
        document = {
            "key": key,
            "dias": dias,
            "usuario": usuario,
            "expiracion": expiracion.strftime("%Y-%m-%d %I:%M:%S %p"),
            "fecha": now,
            "status": "on"
        }
        self._key_collection.insert_one(document)

    def init_rangos(self):
        _collection = self._db['rangos']

        rangos_data = [
            {"Numero": 1, "Rango": "Mod", "Priv": "Limited", "Obsequiar": ["Admin", "Dev", "Owner"]},
            {"Numero": 2, "Rango": "Seller", "Priv": "Standard", "Obsequiar": []},
            {"Numero": 3, "Rango": "Admin", "Priv": "High", "Obsequiar": []},
            {"Numero": 4, "Rango": "Dev", "Priv": "High", "Obsequiar": []},
            {"Numero": 5, "Rango": "Hunter", "Priv": "Medium", "Obsequiar": []},
            {"Numero": 6, "Rango": "Owner", "Priv": "Maximum", "Obsequiar": []}
        ]

        operations = []
        for rango in rangos_data:
            operations.append(
                UpdateOne({"Numero": rango["Numero"]}, {"$set": rango}, upsert=True)
            )
        result = _collection.bulk_write(operations)
        return result.bulk_api_result


def querygrup(id: int = 0):
    return MondB(idchat=id).querygrup()

def queryUser(id: int = 0):
    return MondB(idchat=id).queryUser()

def savedbuser(id: int = 0, username: str = "", name: str = ""):
    return MondB(id=id, username=username, name=name).savedbuser()

def querycora(id: int = 0):
    return MondB(idchat=id).querycora()

def savecora(id: int = 0):
    return MondB(idchat=id).savecora()

def savelang(id: int = 0, username: str = "", name: str = ""):
    return MondB(id=id, username=username, name=name).savelang()
