## Instalar pymongo
## pip install pymongo

#Importar libreria
from pymongo import MongoClient
import json

# Conexión al servidor local de MongoDB
client = MongoClient('localhost', 27017)

#Revisamos las bases de datos disponibles
print(client.list_database_names())

# Conexión a la base de datos
db = client['test']

#Revisamos las colecciones disponibles
print(db.list_collection_names())

#Creamos una nueva colección
collection = db['Muestras_CO2'] # Se crea cuando se le agregan documentos

#Agregamos el archivo json a la colección
with open('./datos/owid-co2-data.json') as f:
    file_data = json.load(f)

# Insertar los datos en la colección
collection.insert_many(file_data)
#Revisamos la cantidad de documentos en la colección
print(collection.count_documents({}))
