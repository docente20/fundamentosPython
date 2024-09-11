'''
Juan y María están haciendo un programa para jugar a los dados con las siguientes 
reglas:

Si sale 1, vuelven a lanzar.
Si sale 6, quedan empatados.
Si sale 2 ó 3 gana Juan.
Si sale 4 ó 5 gana María.
Escribe el programa en Python utilizando el condicional para escribir el 
mensaje según el resultado de lanzar el dado.

Vamos a intentar obtener el número de forma aleatorio usando la función random


'''

print("Programa para jugarlos dados")

import random

numero = random.randint(1,6)
random.r

print(f"Sacaste un : {numero}")

if numero == 1:
    print("Vuelve a lanzar")
elif (numero==2 or numero ==3 ):
    print("Gana Juan")
elif (numero==4 or numero == 5):
    print("Gana María")
else:
    print("Quedan empatados")