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
    primera=True
    años = filtroFicheros(ini, fin)
    for año in años:
        path = carpeta+año
        dt = cargarDT(path)
        if primera:
            dtTotal = dt
            primera=False
        else:
            dtTotal = dtTotal.add(dt, fill_value=0)

    dtTotal.sort_values("cuenta", ascending=False, inplace=True)
    print(dtTotal.head(10))    


def concatenarRangoAños(ini, fin):
    """Concatenar todos los dt de cada año y exportarlo a otro fichero"""
    años = filtroFicheros(ini, fin)
    L = [pd.read_csv(carpeta+año, header=None, names=['nombre','sexo','cuenta'])  for año in años]
    dtTotal = pd.concat(L, ignore_index=True)
    dtTotal.sort_values(by='nombre', inplace=True)
    print(dtTotal.head(20))

if __name__ == '__main__':
    concatenarRangoAños(1990, 1992)

