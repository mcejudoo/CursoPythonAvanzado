"""
Exportar registros de la BD a json / xml
"""

import json
from base_datos import BaseDatos, Producto, Categoria, path

def testJSON():
    bd = BaseDatos(path)
    L = bd.select()    
    d = [p.to_json() for p in L]

    # Convertir la lista de objetos a un formato json y pasarlo a un str. (visualizarlo con indentación)
    cad = json.dumps(d, indent=4)
    print(cad)

    d2 = json.loads(cad)
    print(d2[0], type(d2[0]))
    obj = Producto.create(d2[0])
    print(obj, type(obj))


def testXML():
    pass

if __name__ == "__main__":
    testJSON()