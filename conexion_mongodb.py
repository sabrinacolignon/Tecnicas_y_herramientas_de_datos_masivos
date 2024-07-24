import pymongo
from pymongo import MongoClient


#username = input('Ingrese el nombre de usuario: ')
#password = input('Ingrese la contraseña: ')

client = MongoClient('mongodb://192.168.23.124:27017/',
                        username='user01',
                        password='1234',
                        #authSource='test-database'
                        )

#db = client.test_database
db = client['test-database']
#collection = db.test_collection
collection = db['usuarios']

alumno= {"nombre": "josefina", "edad":20}
collection.delete_one(alumno)

client.close()