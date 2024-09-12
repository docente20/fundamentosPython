mensaje = "Hola mundo"
longitud = len(mensaje)
tamano = len("Buenas tardes")
#print(f"Longitud cadena1 {longitud} caracteres")
#print(f"Longitud cadena2 {tamano} caracteres ")
#print("La longitud de la cadena 1 es ", longitud , " caracteres" )

#Asignación operador +=
dato = "Bienvenidos a"
dato += " - "
dato += "El curso de logica de programación"
#print(dato)

#Concatenar Unir dos cadenas o más para formar una cadena de mayor tamaño
mensaje1 ="Bienvenidos a"
mensaje2 = " - "
mensaje3 = "el curso de lógica de programación"
mensajeConcatenado = mensaje1 + mensaje2 + mensaje3
#print(mensajeConcatenado)

#Buscar: localizar dentro de una cadena, una subcadena más pequeña 
# a un caracter
mensajeBusqueda = "Bienvenidos a el curso de lógica de programación"
buscar = mensajeBusqueda.find("lógica")
#print(buscar)

#extraer:  sacar una porción de la cadaena original, según su posición dentro de ella

mensajeExtraer = "Bienvenidos a el curso de lógica de programación"
extraer = mensajeExtraer[0:15]
#print(extraer)

#comparación
#lower() Minusculas upper() convierte en Mayusculas
nombre1 = "FABIO".upper()
nombre2 = "FaBio".upper()
print(nombre1)
print(nombre2)

comparar = nombre1 == nombre2
print(comparar)
