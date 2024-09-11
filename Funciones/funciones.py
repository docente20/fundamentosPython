#Sintaxis de la función
'''
def nombreFuncion():
    #cuerpo de la función
    #código que se ejecuta cuando se a la función

nombreFuncion()

'''

#Función sin parámetro ni retorno
def saludar():
    print("Hola, Bienvenidos a Python")


#saludar()

#Función con parámetro sin retorno
def sumar(a,b):
    resultado = a+b
    print(f"La suma de {a} y {b} es {resultado} ")


#llamar a la función con argumentos o parametros
# num1 = int(input("Ingrese número 1: "))
# num2 = int(input("Ingrese número 2: "))
# sumar(num1,num2) 

#Funcion con retorno de valor
def multiplicar(x,y):
    resultado = x*y
    return resultado

num1 = int(input("Ingrese número 1: "))
num2 = int(input("Ingrese número 2: "))
resultadoMul = multiplicar(num1,num2)
print(resultadoMul)
print(f"El resultado es: {multiplicar(num1, num2)}")