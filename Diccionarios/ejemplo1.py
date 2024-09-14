#Estructura de un diccionario
diccionario = {"nombre":"Carlos",
               "edad":22,
               "cursos":["Python","Metodologia","Socioemocional"]
               }

#Acceder a los elementos del diccionario por medio de la clave
print(diccionario["nombre"])
print(diccionario["edad"])
print(diccionario["cursos"])

#Acceder a los elementos de la lista contenida en el diccionario
print(diccionario["cursos"][0])
print(diccionario["cursos"][1])
print(diccionario["cursos"][2])

#Acceder por medio de la función get(clave)
valor = diccionario.get("edad")
print(valor)