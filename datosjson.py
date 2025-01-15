# Script: datosjson.py

import json  # Importar la biblioteca JSON para manejar archivos JSON

# Ruta del archivo JSON
json_path = "/home/devasc/labs/devnet-src/parsing/myfile.json"

try:
    # Abrir y leer el archivo JSON
    with open(json_path, "r") as file:
        # Cargar el contenido del archivo JSON en la variable json_file
        json_file = json.load(file)
    
    # Confirmar que el archivo se cargó correctamente
    print("El archivo JSON se cargó correctamente.")
    print("Contenido del archivo JSON:")
    print(json.dumps(json_file, indent=4))  # Imprime el contenido formateado (opcional)

except FileNotFoundError:
    print(f"Error: No se encontró el archivo en la ruta especificada: {json_path}")
except json.JSONDecodeError:
    print(f"Error: El archivo {json_path} no contiene un JSON válido.")
except Exception as e:
    print(f"Ha ocurrido un error inesperado: {e}")
