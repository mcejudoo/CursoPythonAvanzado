"""
Exportar datos de la BD a XML / JSON. 
Parsear el fichero generado con XML / JSON y pruebas con XPath (XML)
"""

from base_datos import BaseDatos, path
from xml.etree.ElementTree import Element, SubElement, Comment, tostring, ElementTree

class ExportarBD:

    def productosToXML(self, L, fichero=None):
        """
        Recibimos una lista de productos para exportar a XML
        """
        try:
            if not fichero:
                fichero = "productos_bd.xml"
            # Creamos un nodo Element por cada producto que nos venga en la lista:
            top = Element('productos')
            top.set('version','1.0')
            comentarios = Comment('productos de la base de datos')
            top.append(comentarios)
            for p in L:
                producto = SubElement(top,'producto')
                producto.attrib['id'] = str(p.id)

                nombre = SubElement(producto, 'nombre')
                nombre.text = p.nombre

                categoria = SubElement(producto, 'categoria')
                categoria.attrib['idcat']=str(p.cat.id)
                categoria.text = p.cat.nombre

                precio = SubElement(producto, 'precio')
                precio.text = "%.2f" % (p.precio,)

                existencias = SubElement(producto, 'existencias')
                existencias.text = str(p.exis) 
            
            tree = ElementTree()
            tree._setroot(top)
            tree.write(fichero)
            print('Generado el fichero: ',fichero)

        except Exception as e:
            print(e)  

    def getProductosXML(self, fichero):
        L = []
        with open(fichero, 'rt'):
            ET = ElementTree()
            tree = ET.parse(fichero)
            top = ET.getroot()
            #print(tostring(top))
            for nodo in tree.iter():
                if nodo.tag == 'nombre':
                    L.append(nodo.text)
        return L

    def productosToJson(self, L, fichero=None):
        """
        Recibimos una lista de productos para exportar a JSON
        """
        pass

def testExportarXML():      
    bd = BaseDatos(path)
    L = bd.select()
    obj = ExportarBD()
    obj.productosToXML(L, "productos.xml")

def testGetProductosXML():
    obj = ExportarBD()
    L = obj.getProductosXML('productos.xml')
    print(L)

if __name__ == '__main__':
    #testExportarXML()
    testGetProductosXML()

