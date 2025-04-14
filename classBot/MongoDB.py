import pymongo
from datetime import datetime

class MondB:
    def __init__(self,
                 id: int = None,
                 name: str = None,
                 username: str = None,
                 idchat: int = None,
                 tipo: str = None,
                 ):
        self.id = id
        self.name = name
        self.username = username
        self.idchat = idchat
        self.tipo = tipo
        self.url = 'mongodb://mongo:AmgoVcezgoCslzqtaMYuHIjXvvdZMnlI@tramway.proxy.rlwy.net:48687'
        self._client = pymongo.MongoClient(self.url, serverSelectionTimeoutMS=5000)
    def queryUser(self):
        _database = self._client['bot']
        _collection = _database['user']
        _consult = {"id": self.idchat}
        return _collection.find_one(_consult)
    def savedbuser(self):
        _database = self._client['bot']
        _collection = _database['user']
        existing_user = _collection.find_one({"_id": self.id})
        if existing_user:
            print(f"El usuario con ID {self.id} ya está registrado.")
            return False
        _save = {
            "_id": self.id,
            "username": self.username,
            "plan": "Free User",
            "role": "User",
            "status": "Libre",
            "credits": 0,
            "antispam": 60,
            "time_user": 0,
            "alerts": 0,
            "since": datetime.now(),
            "key": 'None',
            "lang": "es"
        }
        _collection.insert_one(_save)
        return True

    def savepremium(self):
        _database = self._client['bot']
        _collection = _database['user']
        myquery = {"plan": "Free User"}
        newvalues = {"$set": {"plan": "premium"}}
        _collection.update_one(myquery, newvalues)
def savedbgrup(self, dias: int = None, plan: str = None):
        _database = self._client['bot']
        _collection = _database['group']
        if dias is None:
            if plan is None:
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
        _database = self._client['bot']
        _collection = _database['group']
        _consult = {"id": self.idchat}
        return _collection.find_one(_consult)
def querycora(self):
        _database = self._client['bot']
        _collection = _database['corazon']
        _consult = {"id": self.idchat}
        return _collection.find_one(_consult)
def savecora(self):
        _database = self._client['bot']
        _collection = _database['corazon']
        _consult = {"id": self.idchat}
        return _collection.insert_one(_consult)
def savelang(self):
        _database = self._client['bot']
        _collection = _database['lang']
        _save = {
            "_id": self.id,
            "username": self.username,
            "plan": "Free User",
            "role": "User",
            "status": "Libre",
            "credits": 0,
            "antispam": 60,
            "time_user": 0,
            "alerts": 0,
            "since": datetime.now(),
            "key": 'None',
            "lang": "es"
        }
        return _collection.insert_one(_save)
def querygrup(id: int = None):
    return MondB(idchat=id).querygrup()

def queryUser(id: int = None):
    return MondB(idchat=id).queryUser()

def savedbuser(id: int = None, username: str = None, name: str = None):
    return MondB(id=id, username=username, name=name).savedbuser()

def querycora(id: int = None):
    return MondB(idchat=id).querycora()

def savecora(id: int = None):
    return MondB(idchat=id).savecora()

def savelang(id: int = None, username: str = None, name: str = None):
    return MondB(id=id, username=username, name=name).savelang()
