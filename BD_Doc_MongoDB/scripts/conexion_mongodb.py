import pymongo
from pymongo import MongoClient

client = MongoClient('mongodb://192.168.23.124:27017/',
                        username='user02',
                        password='1234',
                        #authSource='test-database'
                        )
db = client.tuped_database
#db.create_collection('alumnos')
collection = db.alumnos

documento = {
    "nombre": "Sabrina",
    "edad": 25,
    "residencia": 'Oro Verde',
    "año_nac": 1999,
    "tiene_hermanos": True,  # Este campo también se insertará como 'bool'
    "vecino": None,  # Este campo se insertará como 'null'
}
#collection.insert_one(documento)

import pprint
pprint.pprint(collection.find_one({"nombre": "Sabrina"}))	# Busca un documento con el nombre "Sabrina"

client.close()