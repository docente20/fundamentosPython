def ejemplo1():
    lista = [1,3,2,6,7]
    print(lista)
    
#ejemplo1()

def ejemplo2():
    nombres = ["Hugo", "Paco","Luis","Ramiro","Ernesto"]
    print(f"El primer elemento de la lista es: {nombres[0]} ")
    print(f"El ultimo elemento de la lista es: {nombres[-1]} ")
    print(f"Accedo desde una posición a otra de la lista: {nombres[1:4]}")
    print(f"Accedo desde posición 0 a otra de la lista: {nombres[:4]}")
    print(f"Accedo desde posición inical hasta el final de la lista: {nombres[2:]}")
    print(f"Invertir la lista: {nombres[::-1]}")
    print(nombres)

#ejemplo2()

def ejemplo3():
    equipo = ["Argentina","Colombia","Uruguay","Brasil","Ecuador"]
    #Función para insertar un nuevo valor al final de la lista append(valor)
    #equipo.append("Chile")
    
    #Función para insertar elementoss en un punto intermedio insert(pos,valor)
    #equipo.insert(2,"Chile")
    
    #Función que agrega varios elementos a la lista extend([v1, v2,v3...])
    equipo.extend(["Chile","Paraguay","Venezuela"])
    
    #in comprobamos si un elemento se encuentra o no en una lista
    print("Chile1" in equipo)
    
    #Función index(valor) Indica donde está el indice de un elemento
    print(f"Indice : {equipo.index("Paraguay")} ")
    
    #remove(valor) = elimina un valor de la lista
    #equipo.remove("Paraguay")
    
    #Eliminar un valor en la posición i pop(i)
    #equipo.pop(5)
    
    #Eliminar el último valor de la lista pop()
    equipo.pop()
    
    print(equipo)

ejemplo3()
    