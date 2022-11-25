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


# Mapeo de clases y recursos:
# GET: http://localhost:5000/productos/<id>
# GET: http://locaohost:5000/productos
# GET: http://locaohost:5000/productos/categoria/<nombre_categoria>
api.add_resource(ProductoRest, "/productos/<id>")

if __name__ == "__main__":
    app.run(debug=True)
