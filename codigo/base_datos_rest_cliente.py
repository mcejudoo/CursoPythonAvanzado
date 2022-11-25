
from requests import put, get, delete, post
import json
import pandas as pd

URL = "http://localhost:5000/productos"

def testURLs():
    # GET
    print(get(URL+"/105").json())

    # DELETE
    print(delete(URL+"/105").json())

    # POST
    headers = {"Content-Type": "application/json"}
    d = {"id":105,"nombre":"salsa rosa","cat":{"id":2,"nombre":"comidas"},"precio":30.0,"exis":25}
    print(post(URL, data=json.dumps(d), headers=headers).json())

    # PUT
    d = {"id":105,"nombre":"salsa brava","cat":{"id":2,"nombre":"comidas"},"precio":10.0,"exis":250}
    print(put(URL, data=json.dumps(d), headers=headers).json())


def cargaCSVEmpleadosRest(path):
    """Cargar el fichero CSV de empleados a la base de datos utilizando el servicio REST"""
    dt = pd.read_csv(path, sep=';')
    print(dt.head())

    L = dt.to_json(orient='records', lines=True).splitlines()
    print(L)


if __name__ == '__main__':
    path = "../practicas/avanzado2/pandas/merge/Empleados.txt"
    cargaCSVEmpleadosRest(path)