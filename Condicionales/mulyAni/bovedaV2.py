"""
Pedro y Juan son dos hermanos, hijos únicos de Simón, y quienes tienen 
acceso a una bóveda en un exclusivo banco. El dueño original de esta bóveda 
es su padre, y en su testamento ha especificado las siguientes condiciones 
para que el banco le permita acceder a sus hijos al contenido de dicha bóveda. Las condiciones son las siguientes:

a. Juan debe ser mayor de 35 años, O Pedro debe ser menor de 50 años.
b. La suma de sus edades debe ser un número par.
c. Simón debe tener mínimo 1 nieto.
Construye un algoritmo que lea la edad de Juan, la edad de Pedro 
y el número de nietos y calcule, usando condicionales, 
si tienen acceso (SI) o no (NO) a la bóveda.

CONDICIONALES ANIDADOS
"""


edadJuan = int(input("Ingrese edad de Juan: "))
edadPedro = int(input("Ingrese edad de Pedro: "))
nietos = int(input("Ingrese el número de nietos de Simón: "))
sumaEdad = edadJuan + edadPedro

if (edadJuan > 35 or edadPedro < 50): # V
    if sumaEdad % 2 == 0: # F
        if nietos >= 1: # F
            print("Tiene acceso a la Boveda")
        else:
            print("No tiene acceso porque Simón no tiene nietos aún")
    else:
        print("La suma de edades no es un número par")
else:
    print("Las Edades de Juan y Pedro no cumplen")
            
