#Escribe un programa que reciba una palabra y diga cuántas letras
#'a' posee y muestre por pantalla el numero de veces que aparece la letra
#en la palabra

palabra = input("Ingrese una palabra: ").lower()#Araña = araña
contL = 0 # 0
for letra in palabra: #letra = araña letra=
    if letra == "a":#v
        contL+=1#0 + 1 =1
print(f"La cantidad de letras 'a' que tiene la palabra {palabra} es {contL} ")

#utilizando la función count()
print(palabra.count('a'))

