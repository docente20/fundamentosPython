#Dividir dos numeros donde el divisor no debe ser 0 ni negativo

dividendo = float(input("Digite el valor del dividendo: "))
divisor = float(input("Digite el valor del divisor: "))
contIntentos = 0#0
while divisor <= 0:#0 <= 0 F
    print(f"El divisor no puede ser 0 ni negativo {divisor} ")
    if contIntentos == 2:# 0 ==  2 F
        print("La cantidad de intentos superó el límite")
        break #romper el ciclo
    divisor = float(input("Digite el valor del divisor: "))#6
    contIntentos+=1 #0 + 1 = 1

if contIntentos < 2:#1<2
    resultado = dividendo/divisor
    print(f"El resultado de la división es {resultado:,.3f}  ")
    

