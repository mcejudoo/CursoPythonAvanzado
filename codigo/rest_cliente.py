
from requests import put, get, delete, post
import json

URL = "http://localhost:5000/productos"

# GET
print(get(URL+"/105").json())

# DELETE
print(delete(URL+"/105").json())

# POST
headers = {"Content-Type": "application/json"}
d = {"id":105,"nombre":"salsa rosa","cat":{"id":2,"nombre":"comidas"},"precio":30.0,"exis":25}
print(post(URL, data=json.dumps(d), headers=headers).json())

# PUT
d = {"id":105,"nombre":"salsa brava","cat":{"id":2,"nombre":"comidas"},"precio":10.0,"exis":250}
print(put(URL, data=json.dumps(d), headers=headers).json())