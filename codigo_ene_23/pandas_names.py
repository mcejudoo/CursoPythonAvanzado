"""
Prácticas con los ficheros de los nacimientos de EEUU
"""

import pandas as pd
import os

carpeta = "../practicas/avanzado2/pandas/names/"

def cargarDT(path):
    dt = pd.read_csv(path, header=None, names=['nombre','sexo','cuenta'])
    dt.set_index(["nombre","sexo"], inplace=True)
    return dt

def testSuma2():
    dt1 = cargarDT(carpeta+"yob1990.txt")
    dt2 = cargarDT(carpeta+"yob1991.txt")
    r = dt1.add(dt2, fill_value=0)
    r.sort_values("cuenta", ascending=False, inplace=True)
    print(r.head())

def filtroFicheros(ini, fin):
    L = []
    for f in os.listdir(carpeta):
        t = f.partition('.')
        if t[2] == 'txt':
            año = int(t[0][-4:])
            if ini <= año <= fin:
                L.append(f)
    return L


def sumaRangoAños(ini, fin):
    años = filtroFicheros(ini, fin)
    print(años)

if __name__ == '__main__':
    sumaRangoAños(1990, 2000)

