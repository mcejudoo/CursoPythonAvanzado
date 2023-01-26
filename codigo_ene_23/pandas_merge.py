"""
Unir ficheros CSV por filas como si fuera la operación join
"""

import pandas as pd

carpeta = "../practicas/avanzado2/pandas/merge/"


def recuentos(path):
    dtPed = pd.read_csv(path+"Pedidos.txt", sep=';')
    # Número de pedidos por país:
    print(dtPed.pais.value_counts()) # A una columna -> Serie (número de pedidos por país)
    print()
    print(dtPed.value_counts()) # Aplicado al DataFrame (contar filas repetidas)
    print()
    print(dtPed[['pais','cliente']].value_counts()) # Número de pedidos por país y cliente



def join(path):
    dtPed = pd.read_csv(path+"Pedidos.txt", sep=';')
    dtEmp = pd.read_csv(path+"Empresas.txt", sep=';')
    dtE = pd.read_csv(path+"Empleados.txt", sep=';')
   
    dtPed_Emp = pd.merge(dtPed, dtEmp, left_on='idempresa',right_on='id')
    dtFinal = pd.merge(dtPed_Emp, dtE, left_on='idempleado',right_on='id')
    #pd.set_option('display.max_rows', None)
    dtFinal = dtFinal[['idpedido','cliente','empresa','nombre','importe','pais','idempresa']]
    dtFinal.rename(columns={"nombre":"empleado"}, inplace=True)
    print(dtFinal.head())

    # Agrupar por empresa y empleado y calcular suma de importe
    print(dtFinal.importe.groupby([dtFinal.empresa, dtFinal.empleado]).sum())

    # Agrupar por pais y calcular la media

    print(dtFinal.groupby(["empresa", "empleado"]).sum())

    
if __name__ == '__main__':
    #join(carpeta)
    recuentos(carpeta)