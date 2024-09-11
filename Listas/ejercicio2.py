'''
Actividad 2. Dado una lista de 10 posiciones, crea un algoritmo que lea y escriba 
cada uno de sus elementos.
'''

def actividad2():
    productos = []#Crea una lista vacia
    for i in range(5): #i=5
        nombre = input(f"Ingrese el nombre del producto {i+1} ")
        productos.append(nombre) #productos["Manzana","Fresas","Patilla","Mango",Pera]
    print(productos)
        

actividad2()
