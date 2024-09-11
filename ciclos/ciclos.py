#CICLOS: Permiten repetir instrucciones en funión de ciertas condiciones
#Ciclo while - mientras que
#Ciclor for - para
#Ciclo do while - hacer hasta


#estructura
'''
while condicion:
    instruccion 1
    instruccion 2

'''
#forma determinada
i = 1 #i=1
#     6 <= 5 f
# while i <= 20:
#     print(f"iteración No {i} ")
#     i+=2 # i = 5 +1  6


print("Esto está por fuera del ciclo")

#ciclo indeterminado
salario = int(input("Ingrese por favor su salario: "))
while salario < 0:#V
    print("Vuelve a intentar... Salario no puede ser negativo")
    salario = int(input("Ingrese por favor su salario: "))

print(f"Su salario es {salario:,.0f} ")

