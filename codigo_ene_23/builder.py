"""
Implementación del patrón Builder. Conversor de un fichero CSV a HTML
"""

import abc

class Director:
    
    def __init__(self, builder):
        self.builder = builder

    def convertirFichero(self, path):
        pass

class Builder(abc.ABC):

    @abc.abstractmethod
    def createCab(self, texto):
        pass

    @abc.abstractmethod
    def createDetalle(self, texto):
        pass

class BuilderHTML(Builder):

    def createCab(self, texto):
        pass

    def createDetalle(self, L):
        """
        Devuelve el formato:
        <tr><td>col1</td><td>col2</td><td>col3</td></tr>
        """
        return "<tr>"+"".join(["<td>"+str(i)+"</td>" for i in L])+"</tr>"


