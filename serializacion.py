"""
Serializar objetos complejos de Python.
"""

import pickle as p
from base_datos import BaseDatos, path

def serializar(L, fichero, formato="pickle"):
    f = None
    try:
        f = open(fichero, 'wb')
        if formato == "pickle":
            p.dump(L, f)
        else:
            pass

        print('Generado el fichero: ', fichero)

    except Exception as e:
        print(e)

    finally:
        if f: f.close()

def deserializar(fichero, formato="pickle"):
    pass

if __name__ == '__main__':
    bd = BaseDatos(path)
    L = bd.select()    
    serializar(L, "productos.bin")
    L2 = deserializar("productos.bin")
    for i in L2[:5]:
        print(i)

