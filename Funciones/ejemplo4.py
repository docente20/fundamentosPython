#Crear una función que pregunte la edad del usuario y determine si puede
# votar

def verificarVotante():
    edad = int(input("Ingrese su edad: "))
    
    if edad >= 18:
        print("Eres apto para votar")
    else:
        print("Aún no puedes votar")


verificarVotante()