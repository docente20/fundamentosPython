'''
Actividad 1:  Usted es cajero en un supermercado de su ciudad. 
Su trabajo es imprimir cada uno de los productos de su cliente, 
su precio y calcular el total a pagar.
Diseña un programa con las siguientes características:
1. Que tenga una función caja que solicite al usuario nombre y 
precio de cada producto.
2. Una variable total que vaya sumando el precio de los artículos
3. Una función adicional llamada imprimaProducto(nombre, precio) 
que reciba el nombre y el precio de cada producto y los imprima.
4. Que después de llamar a imprimaProducto le pregunte al usuario 
si tiene o no más artículos a ingresar. Si no tiene, el programa 
debe detenerse.
5. Si no hay más artículos, que imprima el total de la compra
Al final de tus funciones, puedes simplemente llamar a la función 
caja para probar: caja()

'''
def imprimaProducto(nombre, precio):
    print(f"Producto {nombre}: ${precio}" )

def caja():
    nombreProd = input("Ingrese nombre del producto: ")
    precioProd = int(input(f"Ingrese precio del producto {nombreProd}: "))
    total=precioProd#100000
    imprimaProducto(nombreProd,precioProd)
    while True:
        respuesta = input("¿Desea ingresar más productos?[si - no] : ").lower()
        if respuesta.strip() == "si":#f Strip Este método se utiliza para eliminar todos los espacios en blanco iniciales y finales de una cadena
            nombreProd = input("Ingrese nombre del producto: ")
            precioProd = int(input(f"Ingrese precio del producto {nombreProd}: "))
            total+=precioProd#10000+7000=17000
            imprimaProducto(nombreProd,precioProd)
        else:
            break
    print(f"El total de la compra es {total}")
            
caja()