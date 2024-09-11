#Crear una función que pida al usuario ingresar varios números
#y calcule el promedio

def calcularPromedio():
    cantidad = int(input("¿cúantos números desea ingresar?: "))
    while True:
        if cantidad <= 0:
            print("Error no puedo hallar promedios")
            cantidad = int(input("¿cúantos números desea ingresar?: "))
        else:
            suma = 0
            i=1
            while i<=cantidad: #4 <=3 f
                numero =  float(input(f"ingrese el número {i}: "))
                suma += numero # suma = 14 + 7 = 21
                i+=1 #i = 3 + 1 =4
            promedio =  suma/cantidad
            print(f"El promedio de los números es: {promedio:,.2f} ")
            respuesta = input("¿Desea seguir calculando promedios?[si o no] ").lower()
            if respuesta != "si":
                break
            cantidad = int(input("¿cúantos números desea ingresar?: "))


calcularPromedio()
        
    