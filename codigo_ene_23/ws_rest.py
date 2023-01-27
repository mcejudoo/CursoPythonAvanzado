from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
	def get(self):
		return{"hello": "world"}

# Mapeo entre un recurso (la clase) y un petición
api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
	app.run(debug=True)
