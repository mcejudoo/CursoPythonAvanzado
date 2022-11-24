"""
Serializar objetos complejos de Python.
"""

import pickle as p
from base_datos import BaseDatos, path

def serializar(L, fichero):
    f = None
    try:
        f = open(fichero, 'wb')
        p.dump(L, f, 2)    
        print('Generado el fichero: ', fichero)
    except Exception as e:
        print(e)
    finally:
        if f: f.close()

def deserializar(fichero):
    f = None
    try:
        f = open(fichero, 'rb')       
        return p.load(f)      
    except Exception as e:
       print(e)
    finally:
        if f: f.close()        


if __name__ == '__main__':
    bd = BaseDatos(path)
    L = bd.select()    
    serializar(L, "productos.bin")
    L2 = deserializar("productos.bin")
    for i in L2[:5]:
        print(i)

   

