#Escribe una función llamada esPar que reciba un número como parámetro
#y devuelva True si el número es par y False si es impar

def esPar(numero):
    return numero % 2 == 0


num  = int(input("Ingrese número: "))
print(esPar(num))
