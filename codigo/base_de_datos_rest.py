"""
Servidor REST para implementar un API REST: con las operaciones CRUD 
"""

from flask import Flask, make_response, jsonify
from flask_restful import Resource, Api, abort
from base_datos import BaseDatos, path, Producto, Categoria

app = Flask(__name__)
api = Api(app)

class ProductoRest(Resource):

    def get(self, id):
        """
        Recupera un producto de la base de datos
        """
        try:
            bd = BaseDatos(path)
            producto = bd.read(id)
            return make_response(jsonify(producto.to_json()),200)        
        except Exception as e:
            abort(404, message=str(e))


    def delete(self, id):
        """
        Eliminar un recurso de la base de datos
        """
        try:
            bd = BaseDatos(path)
            producto = bd.read(id)
            d = {"Producto eliminado":producto.nombre}
            bd.delete(id)
            #return make_response(jsonify(d),200)        
            return d
        except Exception as e:
            abort(404, message=str(e))


class ProductosList(Resource):

    def get(self):
        """
        Recuperar todos los productos de la base de datos
        """
        bd = BaseDatos(path)
        productos = bd.select()
        L = [p.to_json() for p in productos]
        return make_response(jsonify(L),200)

class ProductosCategoriasList(Resource):

    def get(self, cat):
        """
        Recuperar todos los productos de la base de datos
        """
        bd = BaseDatos(path)
        productos = bd.select(cat)
        L = [p.to_json() for p in productos]
        return make_response(jsonify(L),200)


# Mapeo de clases y recursos:
# GET: http://localhost:5000/productos/<id>
# DELETE: http://localhost:5000/productos/<id>
# GET: http://locaohost:5000/productos
# GET: http://locaohost:5000/productos/categoria/<nombre_categoria>
api.add_resource(ProductoRest, "/productos/<id>")
api.add_resource(ProductosList, "/productos","/productos/")
api.add_resource(ProductosCategoriasList, "/productos/categoria/<cat>")

if __name__ == "__main__":
    app.run(debug=True)
