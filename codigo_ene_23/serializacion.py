"""
Serialización de objetos con pickle y Shelve
"""

import pickle as p
import shelve
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

def testShelveWrite():        
    try:
        bd = BaseDatos(path)
        L = bd.select('comidas')    
        L2 = bd.select('bebidas')    
        shelf = shelve.open('productos2')
        shelf['comidas'] = L
        shelf['bebidas'] = L2
        shelf.close()
    except Exception as e:
        print(e)
   
def  testShelveRead():
    try:
        shelf = shelve.open('productos2')
        L2 = shelf['bebidas']
        L = shelf['comidas']     
        shelf.close()
        print('comidas: ')
        print(L[:2])
        print('bebidas: ', L2[:2])

    except Exception as e:
        raise e
        print(e)



if __name__ == '__main__':
    #testPickleDump()
    #testPickleLoad()
    testShelveWrite()
    testShelveRead()