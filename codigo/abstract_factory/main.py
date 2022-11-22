"""
Utiliza el patrón abstract Factory e incorpora una función para crear la Factoría
elegida
"""
import sys
from factorias import *

def seleccionarFactoria(fab):
    """
    Método de fabricación. Crea la factoría concreta
    """
    try:
        nombreClass = f"Factoria{fab.capitalize()}()" 
        return eval(nombreClass)

    except Exception as e:
        raise ValueError("No existe el fabricante: "+ fab)
    

if __name__ == '__main__':
    try:
        if len(sys.argv) == 2:
            fabricante = sys.argv[1]
        else:
            fabricante = "samsung"    

        fact = seleccionarFactoria(fabricante)
        phone = fact.createSmartPhone()
        phone.call()

        tablet = fact.createTablet()
        tablet.internet()

    except Exception as e:
        print(e)