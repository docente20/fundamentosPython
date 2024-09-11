"""
Pedro y Juan son dos hermanos, hijos únicos de Simón, y quienes tienen 
acceso a una bóveda en un exclusivo banco. El dueño original de esta bóveda 
es su padre, y en su testamento ha especificado las siguientes condiciones 
para que el banco le permita acceder a sus hijos al contenido de dicha bóveda. Las condiciones son las siguientes:

a. Juan debe ser mayor de 35 años, O Pedro debe ser menor de 50 años.
b. La suma de sus edades debe ser un número par.
c. Simón debe tener mínimo 1 nieto.
Construye un algoritmo que lea la edad de Juan, la edad de Pedro 
y el número de nietos y calcule, usando condicionales, 
si tienen acceso (SI) o no (NO) a la bóveda.

operadores lógicos
y -> and
o -> or
no -> not !

Reglas del and(y)
p and q resultado (Las dos condiciones deben ser verdaderas)
V     V = V
V     F = F
F     V = F
F     F = F

Regla del or(o)
p or q resultado (Cualquiera de las dos condiciones debe ser verdadera)
V     V = V
V     F = V
F     V = V
F     F = F
1 escenario: 35 juan < 35  50 pedro < 50 sumaedad = 85 nietos 2
2 escenario juan 36  pedro 40  sumaEdad 76  nietos 3
3 escenario juan 24  perdo 60 sumaEdad 84  nietos 0

"""
edadJuan = int(input("Ingrese edad de Juan: "))
edadPedro = int(input("Ingrese edad de Pedro: "))
nietos = int(input("Ingrese el número de nietos de Simón: "))
sumaEdad = edadJuan + edadPedro
#        f        or   f = F        and         v           and       F   = F
if (edadJuan > 35 or edadPedro < 50) and (sumaEdad % 2 == 0) and (nietos >= 1):
    print("Tienen acceso a la boveda")
else:
    print("No tienen acceso a la boveda")
    

