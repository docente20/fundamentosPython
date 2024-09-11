edad = int(input("Ingrese su edad: "))
if edad >= 0: #v
    if edad < 2: #f
        print("Infante")
    elif edad < 12:#f
        print("Niño")
    elif edad < 18: #f
        print("adolescente")
    elif edad < 60:#v
        print("Adulto")
    else:
        print("Adulto mayor")
else:
    print("Edad no válida")