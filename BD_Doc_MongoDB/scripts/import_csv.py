import csv
import json

# Leer el archivo CSV y convertirlo a una lista de diccionarios
datos = []
with open("./datos/owid-co2-data.csv", 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # Convertir los valores numéricos a tipos de datos apropiados
        for key, value in row.items():
            try:
                row[key] = int(value)
            except ValueError:
                try:
                    row[key] = float(value)
                except ValueError:
                    pass  # El valor no es numérico, lo dejamos como está
        datos.append(row)

# Escribir la lista de diccionarios como JSON en un archivo
with open("./datos/owid-co2-data.json", 'w') as jsonfile:
    json.dump(datos, jsonfile, indent=4)
