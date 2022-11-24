"""
Exportar datos de la BD a XML / JSON. 
Parsear el fichero generado con XML / JSON y pruebas con XPath (XML)
"""

from base_datos import BaseDatos, path
from xml.etree.ElementTree import Element, SubElement, Comment, tostring, ElementTree
from xml.etree.ElementTree import iterparse
import json

class ExportarBD:

    eventos = ['start','end']

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

    def getProductosXMLDom(self, fichero):
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

    def getProductosXMLSax(self, fichero):
        L = []
        for (evento, nodo) in iterparse(fichero, ExportarBD.eventos):
            if evento == 'start' and nodo.tag == 'nombre':
                L.append(nodo.text)
        return L

    def getProductosJSON(self, fichero):
        pass

    def productosToJson(self, L, fichero=None):
        """
        Recibimos una lista de productos para exportar a JSON
        """
        if not fichero:
            fichero = "productos.json"

        f = None
        try:
            productos = []
            for p in L:
                dict_cat = p.cat.__dict__
                p.__dict__['cat'] = dict_cat
                productos.append(p.__dict__) 
            f = open(fichero, "w")
            json.dump(productos, f)           
            return json.dumps(productos, indent=4)
        except Exception as e:
            print(e)
        finally:
            if f:f.close()

def testExportarXML():      
    bd = BaseDatos(path)
    L = bd.select()
    obj = ExportarBD()
    obj.productosToXML(L, "productos.xml")

def testGetProductosXMLDom():
    obj = ExportarBD()
    L = obj.getProductosXMLDom('productos.xml')
    print(L)

def testGetProductosXMLSax():
    obj = ExportarBD()
    L = obj.getProductosXMLSax('productos.xml')
    print(L)

def testGetProductosJson():
    bd = BaseDatos(path)
    L = bd.select()
    obj = ExportarBD()    
    cad_json = obj.productosToJson(L)
    print(cad_json)

if __name__ == '__main__':
    #testExportarXML()
    #testGetProductosXMLDom()
    #testGetProductosXMLSax()
    testGetProductosJson()

