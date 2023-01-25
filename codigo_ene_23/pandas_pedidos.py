"""
Prácticas con pandas
"""

import pandas as pd

path='ficheros_templates/Pedidos.txt'

def exportarPedidos():
    """
    Cargar el fichero de pedidos y crear un nuevo fichero por cada país, incluyendo
    sus pedidos. 
    """
    dt = pd.read_csv(path, sep=';')
    L = dt.pais.unique()
    for p in L:
        pais = p.replace(' ', '_')
        path_destino = f'pedidos_pais/{pais}.csv'

        dtAux = dt[dt.pais==pais]
        dtAux.to_csv(path_destino, sep=';', index=False, decimal=',')
        print('Generando fichero:', path_destino)


def nuevasColsYFormatos():
    """
    Crear nuevas cols y exportar a formatos: xlsx, json, html
    """
    dt = pd.read_csv(path, sep=';')

    # Añadir nuevas cols:
    dt['porc_iva'] = 21.0
    dt['iva'] = round(dt.importe * dt.porc_iva / 100, 2)

    # Añadir una col: Total
    dt['total'] = dt.importe + dt.iva
    dt = dt[['idpedido','cliente','pais','importe','porc_iva','iva','total']]
    dt.to_excel('pedidos.xlsx', index=False)

    print(dt.head())



if __name__ == '__main__':
    #exportarPedidos()
    nuevasColsYFormatos()