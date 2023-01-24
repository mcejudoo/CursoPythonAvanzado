"""
Patrón cadena de responsabilidad
"""

import abc

class Peticion:

    def __init__(self, tipo, contenido):
        self.tipo = tipo
        self.contenido = contenido

    def __str__(self):
        return self.tipo + " " + self.contenido


class Procesador(abc.ABC):

    def __init__(self, sucesor=None):
        self.sucesor = sucesor

    @abc.abstractmethod
    def procesar(self, peticion):
        pass

class ProcesadorEmail(Procesador):

    def procesar(self, peticion):
        if peticion.tipo == 'email':
            print('Enviar por correo: ', peticion.contenido)
        
        elif self.sucesor != None:
            # Propagar la petición al siguiente sucesor:
            print('ProcesadorEmail: propagar la petición')
            self.sucesor.procesar(peticion)

        else:
            print('Fin de cadena ...')


class ProcesadorSMS(Procesador):

    def procesar(self, peticion):
        if peticion.tipo == 'sms':
            print('Enviar por SMS: ', peticion.contenido)
        
        elif self.sucesor != None:
            # Propagar la petición al siguiente sucesor:
            print('ProcesadorSMS: propagar la petición')
            self.sucesor.procesar(peticion)

        else:
            print('Fin de cadena ...')

class ProcesadorWhatsApp(Procesador):

    def procesar(self, peticion):
        if peticion.tipo == 'whatsApp':
            print('Enviar por whatsApp: ', peticion.contenido)
        
        elif self.sucesor != None:
            # Propagar la petición al siguiente sucesor:
            print('ProcesadorWhatsApp: propagar la petición')
            self.sucesor.procesar(peticion)

        else:
            print('Fin de cadena ...')

if __name__ == '__main__':
    peticion = Peticion('email','Contenido del mensaje')
    obj1 = ProcesadorEmail()
    obj2 = ProcesadorSMS(obj1)
    obj3 = ProcesadorWhatsApp(obj2)

    obj3.procesar(peticion)


