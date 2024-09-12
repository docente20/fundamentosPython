#Manejo de cadenas
#Sintanxis: cadena[i:j:k]
#El primer parámetro indica el indice de comienzo de fragmento de cadena
#El segundo parámetro indica el indice final
#El tercer parámetro es opcional y cuando está presente indica el incremento
# con el que se recorrera el camino entre el principio y el fin

cadena = "Bienvenidos a el curso de lógica de programación"
#print(cadena[0:6]) #Cortar el fragmento desde la pos 0 hasta el 6, sin incluirlo
#print(cadena[2:15:2])
#print(cadena[:4])
#print(cadena[4:])
#print(cadena[6:2:-1])
print(cadena[::-1])