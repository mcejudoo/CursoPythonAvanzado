"""
Limpiar el formato de los ficheros
"""
import pandas as pd
carpeta = "../practicas/avanzado2/pandas/csv/"

def limpiarDT(path):
    dt = pd.read_csv(path, sep=';')    

    # Limpiar espacios en blanco del nombre de las columnas.
    dt.columns = [col.strip() for col in dt.columns]
    dt['Lat'] = pd.to_numeric(dt.Lat.str[:-1])
    print(dt.head())
    print()
    print(dt.info())


if __name__ == '__main__':
    limpiarDT(carpeta+"IRMA.csv")