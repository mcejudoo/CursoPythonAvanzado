"""
Unir ficheros CSV por filas como si fuera la operación join
"""

import pandas as pd

carpeta = "../practicas/avanzado2/pandas/merge/"

def join(path):
    dtPed = pd.read_csv(path+"Pedidos.txt", sep=';')
    dtEmp = pd.read_csv(path+"Empresas.txt", sep=';')
    dtE = pd.read_csv(path+"Empleados.txt", sep=';')
   
    dtPed_Emp = pd.merge(dtPed, dtEmp, left_on='idempresa',right_on='id')
    dtFinal = pd.merge(dtPed_Emp, dtE, left_on='idempleado',right_on='id')
    #pd.set_option('display.max_rows', None)
    dtFinal = dtFinal[['idpedido','cliente','empresa','nombre','importe','pais']]
    dtFinal.rename(columns={"nombre":"empleado"}, inplace=True)
    print(dtFinal.head())
    
if __name__ == '__main__':
    join(carpeta)