"""
Serialización de objetos con pickle y Shelve
"""

import pickle as p
from base_datos import BaseDatos, Producto, Categoria, path

def testPickleDump():
    fich = None
    try:
        bd = BaseDatos(path)
        L = bd.select()    
        fich = open('productos.bin',"wb")
        p.dump(L, fich,2)

    except Exception as e:
        print(e)
    finally:
        if fich: fich.close()


def testPickleLoad():
    fich = None
    try:       
        fich = open('productos.bin',"rb")
        L = p.load(fich)
        for pr in L:
            print(pr)

    except Exception as e:
        print(e)
    finally:
        if fich: fich.close()


if __name__ == '__main__':
    testPickleDump()
    testPickleLoad()