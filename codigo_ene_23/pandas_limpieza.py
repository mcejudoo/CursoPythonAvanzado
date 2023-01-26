"""
Limpiar el formato de los ficheros
"""
import pandas as pd
carpeta = "../practicas/avanzado2/pandas/csv/"

def limpiarDT(path):
    dt = pd.read_csv(path, sep=';')    

    # Limpiar espacios en blanco del nombre de las columnas.
    dt.columns = [col.strip() for col in dt.columns]
    dt['Lat'] = pd.to_numeric(dt.Lat.str[:-1], downcast="float")
    dt['Lon'] = pd.to_numeric(dt.Lon.str[:-1], downcast="float")
    dt['Wind'] = pd.to_numeric(dt.Wind.str.replace(" mph",""), downcast='integer')
    dt['Pressure'] = pd.to_numeric(dt.Pressure.str.replace(" mb",""), downcast='integer')
    dt['DateTime'] = pd.to_datetime("2005 " + dt.Date + " " + dt.Time.str.replace(' GMT',''), \
        infer_datetime_format=True)
    dt.drop(columns=['Date','Time'], inplace=True)
    print(dt.head())
    print()
    dt.info()

if __name__ == '__main__':
    limpiarDT(carpeta+"IRMA.csv")