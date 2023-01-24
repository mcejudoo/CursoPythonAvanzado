"""
Ejemplo del patrón decorator. 
"""

import abc

class IVentana(abc.ABC):

    @abc.abstractmethod
    def dibujar(self):
        pass

class Ventana(IVentana):

    def __init__(self,titulo="titulo de la ventana"):
        self.titulo = titulo

    def dibujar(self):
        print(self.titulo, end=' ')


class VentanaDecorator(IVentana):

    def __init__(self, ventana):
        self.ventana = ventana

    def dibujar(self):
        self.ventana.dibujar()

class VentanaDecoratorConBorde(VentanaDecorator):

    def __init__(self, ventana):
        VentanaDecorator.__init__(self,ventana)

    def dibujar(self):
        print(' | ', end=' ')
        VentanaDecorator.dibujar(self)
        print(' | ', end=' ')

class VentanaDecoratorAyuda(VentanaDecorator):

    def __init__(self, ventana):
        VentanaDecorator.__init__(self,ventana)

    def dibujar(self):
        print(' ? ', end=' ')
        VentanaDecorator.dibujar(self)       

class VentanaDecoratorCerrar(VentanaDecorator):

    def __init__(self, ventana):
        VentanaDecorator.__init__(self,ventana)

    def dibujar(self):        
        VentanaDecorator.dibujar(self)       
        print(' X ', end=' ')

if __name__ == '__main__':
    v1 = Ventana('Aplicación')      
    v1.dibujar()
    print()

    
    v2 = VentanaDecoratorAyuda(VentanaDecoratorCerrar(v1))
    v2.dibujar()
    print()

    v3 = VentanaDecoratorConBorde(v2)
    v3.dibujar()
    print()

