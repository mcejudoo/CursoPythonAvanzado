"""
Ejemplo: tipos anotados en Python
"""

def prueba(n1:list,n2:list) -> None:
    print(n1+n2)

def prueba2(cad:str) -> None:
    print(cad.capitalize())


prueba(800,900)
prueba("800","900")
prueba([800,900],[5,6])
 