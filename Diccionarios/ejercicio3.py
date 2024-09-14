'''
Ejercicio 3.
1.	Crea un programa que permita al usuario ingresar información 
de varios estudiantes (nombre, edad, calificación).
2.	El programa debe permitir al usuario:
o	Agregar un nuevo estudiante.
o	Actualizar la calificación de un estudiante existente.
o	Eliminar a un estudiante.
3.	Finalmente, imprime todos los estudiantes y su información.

'''

#Creación del diccionario  vacio
estudiantes = {}

#Función para mostrar el menú de opcion
def menu():
    print("\n**** Menú de Opciones ****")
    print("1. Agregar estudiante")
    print("2. Actualizar Calificación estudiante")
    print("3. Eliminar estudiante")
    print("4. Listar todos los estudiante")
    print("5. Salir")
    print("\n***************************")
    

#menu()
#Agregar estudiantes

def agregarEst():
    id = int(input("Ingrese Id del estudiante: "))
    if id in estudiantes:
        print("El id del estudiante ya existe")
    else:
        nombre = input("Ingrese nombre del estudiante: ")
        edad = int(input("Ingrese edad del estudiante: "))
        calificacion = float(input("Ingrese calificación del estudiante: "))
        estudiantes[id]={"nombre":nombre, 
                         "edad":edad, 
                         "calificacion":calificacion
                         }
        print(f"Estudiante {id} agregado ")
        #print(estudiantes)



def actualizarCalEst():
    id = int(input("Ingrese Id del estudiante a actualizar: "))
    if id in estudiantes:
        nuevaCalificacion =  float(input("Ingresa nueva calificación: "))
        estudiantes[id]["calificacion"]=nuevaCalificacion
        print(f"Calificación del estudiante {id} actualizada ")
        #print(estudiantes)
    else:
        print("El estudiante no existe")
        
    
def eliminarEst():
    id = int(input("Ingrese Id del estudiante a eliminar: "))
    if id in estudiantes:
        del estudiantes[id]
        print(f"Estudiante {estudiantes[id]['nombre']} eliminado ")
        #print(estudiantes)
    else:
        print("El estudiante no existe")
        
def listarEst():
    if estudiantes:
        print("Información de estudiantes")
        for clave, valor in estudiantes.items():
            print(f"Id: {clave}, Nombre:{valor['nombre']}, Edad:{valor['edad']}")
    else:
        print("No hay estudiantes resgistrados")


#Programa principal
while True:
    menu()
    opcion = input("Selecciona una opción: ")
    if opcion == "1":
        agregarEst()
    elif opcion == "2":
        actualizarCalEst()
    elif opcion == "3":
        eliminarEst()
    elif opcion == "4":
        listarEst()
    elif  opcion == "5":
        print("Saliendo.....")
        break
    else:
        print("Opción no valida, seleccione una opción del menú")