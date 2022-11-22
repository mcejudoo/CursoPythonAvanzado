"""
Utiliza el patrón abstract Factory e incorpora una función para crear la Factoría
elegida
"""

def seleccionarFactoria():
    pass


if __name__ == '__main__':
    fact = seleccionarFactoria()
    phone = fact.createSmartPhone()
    phone.call()

    tablet = fact.createTablet()
    tablet.internet()