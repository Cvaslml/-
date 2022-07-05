""""Programa No. 2:
Dado 3 numeros enteros identificar el mayor entre ellos"""

print("--------------------------------------------------------------")
print("-----------------Numero mayor entre 3 enteros-----------------")
print("--------------------------------------------------------------")

#Input
x = int(input("Ingrese el primer numero entero: "))
y = int(input("Ingrese el segundo numero entero: "))
z = int(input("Ingrese el tercer numero entero: "))

#Processing
if x > y and x > z:
    msj = "El primer numero entero es: " + str(x) + " y este es el numero mayor"
if y > x and y > z:
    msj = "El segundo numero entero es: " + str(y) + " y este es el numero mayor"
if z > x and z > y:
    msj = "El tercer numero entero es: " + str(z) + " y este es el numero mayor"

#Output
print(msj)