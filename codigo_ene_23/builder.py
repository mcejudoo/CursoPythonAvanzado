"""
Implementación del patrón Builder. Conversor de un fichero CSV a HTML
"""

import abc

class Director:
    
    def __init__(self, builder):
        self.builder = builder

    def convertirFichero(self, path, sep=';'):
        f=None
        cabs = True
        tabla = ""
        nombre = path.partition('.')[0]
        try:
            f = open(path, "r")
            for linea in f:
                linea = linea.rstrip()
                L = linea.split(sep)
                if cabs:
                    tabla += self.builder.createCab(L)
                    cabs=False
                else:
                    tabla += self.builder.createDetalle(L)

            self.builder.createFichero(tabla, nombre)

        except Exception as e:
            print(e)

        finally:
            if f: f.close()

class Builder(abc.ABC):

    @abc.abstractmethod
    def createCab(self, texto):
        pass

    @abc.abstractmethod
    def createDetalle(self, texto):
        pass

    @abc.abstractmethod
    def createFichero(self, texto, path):
        pass

class BuilderHTML(Builder):

    plantillaHTML = "ficheros_templates/plantilla.html"

    def createCab(self, L):
        return "<tr>"+"".join(["<th>"+str(i)+"</th>" for i in L])+"</tr>"

    def createDetalle(self, L):
        """
        Devuelve el formato:
        <tr><td>col1</td><td>col2</td><td>col3</td></tr>
        """
        return "<tr>"+"".join(["<td>"+str(i)+"</td>" for i in L])+"</tr>"

    def createFichero(self, texto, path):
        tabla = f"<body><table>{texto}</table></body>"

        # Cargar la plantilla
        f=None 
        fout=None 
        path += '.html'      
        try:
            f = open(BuilderHTML.plantillaHTML, "r")
            fout = open(path, "w")
            html = f.read()
            html = html.replace("<body></body>",tabla)    
            fout.write(html)

        except Exception as e:
            print(e)

        finally:
            if f: f.close()     
            if fout: fout.close()       




if __name__ == '__main__':
    builder = BuilderHTML()
    director = Director(builder)
    director.convertirFichero("ficheros_templates/Empleados.txt")
