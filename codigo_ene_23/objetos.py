"""
Ejemplo POO. Traductor de etiquetas
"""

class Traductor:
    """
    Implementación del traductor
    """

    num_instancias = 0

    def __init__(self, idioma='es'):
        path = f"idiomas/{idioma}.txt"
        self.__palabras = self.__carga(path)
        Traductor.num_instancias+=1

    def __carga(self, path):
        fich = None
        d = dict()
        try:
            fich = open(path, 'r')
            for linea in fich:
                linea = linea.rstrip()
                k, _, v = linea.partition('=')
                d[k] = v
            return d

        except Exception as e:
            print(e)

        finally:
            if fich: fich.close()

    @staticmethod
    def getNumInstancias():
        return Traductor.num_instancias

    def getPalabra(self, k):
        return self.__palabras[k]

    def __str__(self):
        return "\n".join([k+" "+v] for k,v in self.palabras.items())

    def __del__(self):
        Traductor.num_instancias-=1
        print(f'Quedan {Traductor.num_instancias} instancias ...')


def test():
    """
    Función para testear el traductor
    """
    t = Traductor()
    print(t.getPalabra('facebook'))
    print('Num instancias: ', Traductor.getNumInstancias())


if __name__ == '__main__':
    test()

    t = Traductor()
    t2 = Traductor()
    print(t.getPalabra('facebook'))
    print('Num instancias: ', Traductor.getNumInstancias())