from pymongo import MongoClient

client = MongoClient("mongodb://mongo:AmgoVcezgoCslzqtaMYuHIjXvvdZMnlI@tramway.proxy.rlwy.net:48687")
db = client["bot"]

try:
    db.create_collection("key", validator={
        "$jsonSchema": {
            "bsonType": "object",
            "required": ["key", "dias", "usuario", "expiracion", "fecha"],
            "properties": {
                "key": {
                    "bsonType": "string",
                    "description": "Aquí van las keys generadas"
                },
                "dias": {
                    "bsonType": "int",
                    "description": "Cantidad de días de validez"
                },
                "usuario": {
                    "bsonType": "string",
                    "description": "Usuario que usó la key"
                },
                "expiracion": {
                    "bsonType": "string",
                    "description": "Fecha de expiración formateada"
                },
                "fecha": {
                    "bsonType": "date",
                    "description": "Fecha de creación en formato Mongo"
                }
            }
        }
    })
    print("✅ Colección 'key' creada con estructura validada.")
except Exception as e:
    print(f"⚠️ Error al crear la colección: {e}")
