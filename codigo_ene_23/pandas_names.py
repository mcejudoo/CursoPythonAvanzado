"""
Prácticas con los ficheros de los nacimientos de EEUU
"""

import pandas as pd

carpeta = "../practicas/avanzado2/pandas/names/"

def cargarDT(path):
    dt = pd.read_csv(path, header=None, names=['nombre','sexo','cuenta'])
    return dt

if __name__ == '__main__':
    dt1 = cargarDT(carpeta+"yob1990.txt")
    dt2 = cargarDT(carpeta+"yob1991.txt")
    r = dt1 + dt2
    print(r.head())

