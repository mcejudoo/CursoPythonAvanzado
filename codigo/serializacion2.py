"""
Serializar objetos complejos de Python.
"""

import shelve
from base_datos import BaseDatos, path

def serializar(L):  
    try:            
        # Cierra automatica:       
        shelf = shelve.open("fichero")
        shelf['datos'] = L   
        shelf.close()       
        print('Generado el fichero')
    except Exception as e:
        print(e.__class__.__name__, e)
       
    finally:
        pass

def deserializar():
    try:          
        shelf = shelve.open("fichero")
        L = shelf["datos"]   
        shelf.close()             
        return L
    except Exception as e:
       print(e.__class__.__name__, e)
       return []
    finally:
        pass    

if __name__ == '__main__':
    bd = BaseDatos(path)
    L = bd.select()    

    
    serializar(L)
    L3 = deserializar()
    for i in L3[:5]:
        print(i)

