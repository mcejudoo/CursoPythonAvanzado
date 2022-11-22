"""
Abstract Factory: Clases relacionadas con los productos
"""

import abc

class SmartPhone(abc.ABC):

    @abc.abstractmethod
    def call(self):
        pass

class S20(SmartPhone):

    def call(self):
        print('S20 realiza una llamada')

class IPhone(SmartPhone):
    
    def call(self):
        print('Iphone realiza una llamada')


class Tablet(abc.ABC):

    @abc.abstractmethod
    def internet(self):
        pass


class GalaxyS20(Tablet):

    def internet(self):
        print('GalaxyS20 se conecta a internet') 


class IPad(Tablet):

    def internet(self):
        print('Tablet se conecta a internet') 


