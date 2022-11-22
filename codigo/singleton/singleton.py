"""
Implementación del patrón singleton para un traductor de idiomas
"""

from os.path import isfile

class Singleton:
    """
    Utiliza un método getInstance para obtener una instancia del traductor
    """
    __idioma = "en"
    __palabras = None

    @staticmethod
    def getInstance(idioma='en'):
        # La primera carga del diccionario o hay un de idioma (refresh)
        if Singleton.__palabras is None or Singleton.__idioma != idioma:
            path = f"{idioma}.txt"
            Singleton.__idioma = idioma
            Singleton.__palabras = Singleton.__cargaFichero(path)            
            print('Se carga el idioma: '+idioma)

        return Singleton.__palabras

    @staticmethod
    def __cargaFichero(path):
        fich = None
        idioma = dict()
        try:
            if not isfile(path):
                print('No existe el fichero ',path)
                path = "en.txt"
                Singleton.__idioma = 'en'

            fich = open(path, 'r')
            for linea in fich:
                linea = linea.rstrip()
                k, _, v = linea.partition('=')
                idioma[k] = v
            return idioma

        except Exception as e:
            raise e

        finally:
            if fich: fich.close()


def testSingleton():
    print(Singleton.getInstance('es')['contacto'])

if __name__ == '__main__':            
    print(Singleton.getInstance('it')['contacto'])
    print(Singleton.getInstance()['facebook'])
    print(Singleton.getInstance()['twitter'])

    testSingleton()
