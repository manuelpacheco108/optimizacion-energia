from pydataxm import* # type: ignore
import csv

objetoAPI = pydataxm.ReadDB()


import csv


with open("collectionsAPI.csv", mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Data Lake"])
    for i in (objetoAPI.get_collections()):
        writer.writerow(objetoAPI.get_collections())  # Ajusta según las variables

