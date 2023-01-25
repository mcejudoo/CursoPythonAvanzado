"""
Cargar el fichero de pedidos y crear un nuevo fichero por cada país, incluyendo
sus pedidos. 
"""

import pandas as pd

path='ficheros_templates/Pedidos.txt'

def exportarPedidos():
    dt = pd.read_csv(path, sep=';')
    L = dt.pais.unique()
    for p in L:
        pais = p.replace(' ', '_')
        path_destino = f'pedidos_pais/{pais}.csv'

        dtAux = dt[dt.pais==pais]
        dtAux.to_csv(path_destino, sep=';', index=False, decimal=',')
        print('Generando fichero:', path_destino)

if __name__ == '__main__':
    exportarPedidos()