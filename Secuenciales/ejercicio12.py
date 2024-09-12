# Ejercicio 12.
# Escribe el código para leer dos números enteros (x, y) de dos dígitos   
# y determina cuánto es igual la suma de todos los dígitos, imprime el resultado. 
# Por ejemplo. x= 45 y= 67. La suma de todos los dígitos es 22.

x = input("Ingrese un número entero de dos digitos: ")
y = input("Ingrese un número entero de dos digitos: ")

# x = "45"
# y = "67"


suma = int(x[0]) + int(x[1]) + int(y[0]) + int(y[1])
print(f"La suma de los digitos es: {suma} ")


