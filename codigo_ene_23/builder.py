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
    def createCab(self, L):
        pass

    @abc.abstractmethod
    def createDetalle(self, L):
        pass

    @abc.abstractmethod
    def createFichero(self, texto, path):
        pass

class BuilderXML(Builder):

    def __init__(self):
        self.cabs = None
        
    def createCab(self, L):
        self.cabs = L
        return ""

    def createDetalle(self, L):
        linea = ""
        for pos, i in enumerate(L):
            linea += f"<{self.cabs[pos]}>"+str(i)+f"</{self.cabs[pos]}>"
        return linea+";"

    def createFichero(self, texto, path):
         # Cargar la plantilla       
        fout=None 
        path2 = path+'.xml'  
        etiqueta = path.split('/')[-1].lower()
        etiquetaReg = etiqueta[:-1].lower()
        try:
            fout = open(path2, 'w')
            regs = texto.split(';')
            xml_final = ""
            for r in regs:
                xml_final += f"<{etiquetaReg}>{r}</{etiquetaReg}>"

            xml = f"<{etiqueta}>{xml_final}</{etiqueta}>"
            xml = "<?xml version='1.0' encoding='UTF-8'?>"+xml              
            fout.write(xml)

        except Exception as e:
            print(e)

        finally:           
            if fout: fout.close()       

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
    #builder = BuilderXML()
    director = Director(builder)
    director.convertirFichero("ficheros_templates/Pedidos.txt")

