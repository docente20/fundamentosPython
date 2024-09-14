'''
Crea un programa que permita al usuario ingresar información 
de varios estudiantes (nombre, edad, calificación). 
El programa debe permitir al usuario: 
•	Agregar un nuevo estudiante. 
•	Actualizar estudiantes 
•	Consultar estudiantes 
•	Eliminar estudiante. 
•	Utilizar validaciones y manejo de errores 
•	Debe ser modular el programa
'''

#Creación lista para almacenar los estudiantes
estudiantes = []

#CRUD = C=Create R= Read U=Update D=Delete
#Función para mostrar el menú de opcion
def menu():
    print("\n**** Menú de Opciones ****")
    print("1. Agregar estudiante")
    print("2. Actualizar estudiante")
    print("3. Consultar estudiante")
    print("4. Eliminar estudiante")
    print("5. Salir")
    print("\n***************************")
    

def agregarEstudiante():
    nombre = input("Ingrese el nombre del estudiante: ").strip()
    while True:
        try:
            edad = int(input("Ingrese la edad del estudiante: "))#25
            if edad <= 0:
                print("La edad debe ser un número positivo")
                continue
            break
        except ValueError:
            print("Entrada inválida. Debe ingresar un número para la edad")
    
    while True:
        try:
            calificacion = float(input(f"Ingrese la calificación del estudiante {nombre}: "))
            if calificacion < 0 or calificacion > 100:
                print("La calificación debe estar entre 0 y 100")
                continue
            break
        except ValueError:
            print("Entrada inválida. Debe ingresar un número para la calificación")
    
    estudiante = {"nombre":nombre, "edad": edad, "calificacion":calificacion}
    estudiantes.append(estudiante)
    print(f"Estudiante {nombre} agregado exitosamente ")
    print(estudiantes)#esto es para probar cada función


def actualizarEstudiante():
    nombre = input("Ingrese el nombre del estudiante a actualizar: ").strip()
    for estudiante in estudiantes:
        if estudiante["nombre"].lower() == nombre.lower():
            print(f"Actualizando información de {nombre}")
            estudiante["edad"] = int(input("Ingrese la nueva edad: "))
            estudiante["calificacion"] = float(input("Ingrese la nueva calificación: "))
            print(f"Información de {nombre} actualizada exitosamente")
            #print(estudiantes) #esto es para probar cada función
            return
    print(f"No encontró ningún estudiante con el nombre {nombre} ")
    
#estudiantes=[{"nombre":"Roberto","edad":25,"calificacion":79},
# {"nombre":"Taliana","edad":35,"calificacion":49}]

#estudiante={"nombre":"Taliana","edad":35,"calificacion":49}


def consultarEstudiante():
    if not estudiantes:
        print("No hay estudiantes registrados")
    else:
        print("\nLista de Estudiantes:")
        for ind, estudiante in enumerate(estudiantes):
            print(f"{ind+1}. Nombre: {estudiante['nombre']}, Edad: {estudiante['edad']}, Calificación: {estudiante['calificacion']}")

        #enumerate permite iterar sobre un lista y obtener tanto el indice de cada elemento
        #como el elemento en si.
        
        #Opcion tradicional
        # for estudiante in estudiantes:
        #     print(f"{estudiante}")

def eliminarEstudiante():
    nombre = input("Ingrese el nombre del estudiante a eliminar: ").strip()
    for estudiante in estudiantes:
        if estudiante["nombre"].lower() == nombre.lower():
            estudiantes.remove(estudiante)
            print(f"Estudiante {nombre} eliminado exitosamente ")
            return
    print(f"No se encontró ningún estudiantes con el nombre {nombre} ")


def principal():
    while True:
        menu()
        opcion = input("Seleccione una opción [1-5]: ")
        if opcion == "1":
            agregarEstudiante()
        elif opcion == "2":
            actualizarEstudiante()
        elif opcion == "3":
            consultarEstudiante()
        elif opcion == "4":
            eliminarEstudiante()
        elif opcion == "5":
            print("Saliendo.....")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 5: ")


principal()