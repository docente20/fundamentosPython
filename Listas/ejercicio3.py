'''
Actividad 3. Dado una lista de N posiciones, calcular la suma de todos sus 
elementos.
'''

def actividad3():
    numeros = []#Inicia una lista vacia
    longitud  = int(input("Ingresa la longitud de la lista: "))
    sumaNum = 0
    for i in range(longitud):#i=3
        num = float(input(f"Digite el elemento {i+1} de la lista: "))
        numeros.append(num)#numeros[56,10,20,14]
        sumaNum += num# 0 + 56 = 56 + 10 = 66 + 20=86+14 = 100
    print(numeros)
    print(f"La suma es: {sumaNum} ")
    
    total = sum(numeros)
    print(f"El total utilizando la funcion sum es: {total} ")

actividad3()
