"""
Prácticas con pandas
"""

import pandas as pd
import sys
import sqlite3 as dbapi
from os.path import isfile

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
    dt.to_json(sys.stdout, indent=4, orient='records')
    dt.to_html('pedidos.html', index=False)

def cargaSQL(path):
    if not isfile(path):
        raise ValueError(path+' no existe')
    else:
        con = dbapi.connect(path)
        sql = """select p.id as idproducto, p.nombre as producto, c.nombre as categoria, p.precio, p.existencias from categorias c 
        inner join productos p on c.id = p.idcategoria"""
        dt = pd.read_sql(sql, con)
        print(dt.head())
        con.close()

if __name__ == '__main__':
    #exportarPedidos()
    #nuevasColsYFormatos()
    cargaSQL('bd/empresa3.db')