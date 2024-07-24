from pymongo import MongoClient
import json

# Conexión al servidor local de MongoDB
client = MongoClient('localhost', 27017)

# Conexión a la base de datos
db = client['THDM_G1']

# Cargar el archivo JSON
with open('./datos/owid-co2-data.json') as f:
    file_data = json.load(f)

# Crear un diccionario para almacenar los documentos por año
documents_by_year = {}

# Asumiendo que cada documento en file_data tiene una clave 'year' que indica el año de registro
for document in file_data:
    year = document.get('year')
    if year:
        if year not in documents_by_year:
            documents_by_year[year] = []
        documents_by_year[year].append(document)

# Insertar los documentos en las colecciones correspondientes
for year, documents in documents_by_year.items():
    collection_name = f'CO2_{year}'
    collection = db[collection_name]
    collection.insert_many(documents)
    print(f'Cantidad de documentos en la colección {collection_name}: {collection.count_documents({})}')

