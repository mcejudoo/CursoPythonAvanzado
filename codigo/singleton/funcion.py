"""
Función de carga de un fichero en un dict
"""

def cargaFichero(path):
    fich = None
    idioma = dict()
    try:
        fich = open(path, 'r')
        for linea in fich:
            linea = linea.rstrip()
            k, _, v = linea.partition('=')
            idioma[k] = v
        return idioma

    except Exception as e:
        print(e)

    finally:
        if fich: fich.close()

if __name__ == '__main__':
    d = cargaFichero('es.txt')
    for k,v in d.items():
        print(k, v)