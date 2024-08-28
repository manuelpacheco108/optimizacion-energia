from pydataxm import pydataxm  # type: ignore
import csv

# Request ´Body´ metodo POST
#{
#   "MetricId": "MetricID",
#   "StartDate": _"YYYY-MM-DD",
#   "EndDate":_"YYYY-MM-DD",
#   "Entity": "Cruce",
#   "Filter":["Listado de codigos"]
#}

def export_api_to_csv(output_file):
    objetoAPI = pydataxm.ReadDB()
    collections = objetoAPI.get_collections()

    with open(output_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        
        # Escribir los nombres de las colecciones como encabezados
        writer.writerow(collections)
        
        # Para cada colección, obtener los datos y escribirlos
        for collection in collections:
            # Asumiendo que hay un método para obtener datos de una colección específica
            # Ajusta esto según la API real
            data = objetoAPI.request_data()
            for item in data:
                writer.writerow(item)

# Uso de la función
export_api_to_csv("output.csv")
