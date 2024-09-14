estudiante = {"nombre":"Juan",
              "edad": 24,
              "carrera":"Ingenieria",
              "promedio":8.5
              }

#Acceder a valores del diccionario
nombreEst = estudiante["nombre"]
print(nombreEst)

edadEst =  estudiante.get("promedio")
print(edadEst)

print(estudiante.get("carrera"))

#Modificar valores en el diccionario
estudiante["edad"]=25

print(estudiante)

#Agregar un nuevo para clave - valor
estudiante["graduado"] = False

print(estudiante)

#Eliminar un par clave - valor con del
#del estudiante["promedio"]
#print(estudiante)

#Eliminar usando función pop()
#estudiante.pop("graduado")
#print(estudiante)

#Recorrer la claves del diccionario
#{'nombre': 'Juan', 'edad': 25, 'carrera': 'Ingenieria', 'promedio': 8.5, 'graduado': False}
for clave in estudiante:#clave = carrera
    print(clave)

#Recorrer la valores del diccionario
#{'nombre': 'Juan', 'edad': 25, 'carrera': 'Ingenieria', 'promedio': 8.5, 'graduado': False}
for valor in estudiante.values():#valor=25
    print(valor)

#Recorrer tanto claves como valores
for clave, valor in estudiante.items():
    print(f"{clave} {valor}")