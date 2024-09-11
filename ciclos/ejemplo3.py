#Diseñar un programa que calcule el promedio de notas del primer
#parcial de un curso de N estudiantes

try:
    nEst = int(input("Digite la cantidad de estudiantes: "))#3
    sumaNota = 0
    i = 1
    while i <= nEst:#1 <= 3
        nota = float(input(f"Digite nota del estudiante {i} "))
        sumaNota+=nota
        i+=1

    promedio = sumaNota/nEst
    print(f"El promedio del curso es {promedio:,.2f}")
except ValueError:
    print("Error, entradas no pueden ser texto sino númericas")
    
#try - except