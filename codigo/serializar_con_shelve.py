import shelve

animales = ["piton", "mono", "camello"]
lenguajes = ["python", "mono", "perl"]
shelf = shelve.open("datos.dat")
shelf["primera"] = animales
shelf["segunda"] = lenguajes
print (shelf["segunda"])
shelf.close()
