'''
Ejercicio 1: Crea un diccionario que almacene la información 
de una lista de productos (nombre del producto, precio y cantidad en stock). 
Realiza las siguientes acciones:
1.	Agrega un nuevo producto al diccionario.
2.	Modifica la cantidad de un producto existente.
3.	Elimina un producto del diccionario.
4.	Imprime el diccionario final.

'''
#Crear el diccionario de productos
productos = {"camisa":{"precio":25000, "cantidad":10},
             "pantalon":{"precio":35000, "cantidad":15},
             "zapatos":{"precio":55000, "cantidad":25}
             }

#print(productos)

#1.	Agrega un nuevo producto al diccionario.
productos["gorra"]={"precio":15000, "cantidad":10}

#print(productos)

#2.	Modifica la cantidad de un producto existente.
productos["gorra"]["cantidad"]=45

#3.	Elimina un producto del diccionario.
del productos["gorra"]
print(productos)
