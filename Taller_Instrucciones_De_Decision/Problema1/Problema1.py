""""Programa No. 1:
Del tiempo dado calcular el valor de llamada"""

print("------------------------------------------------------")
print("-----------------PRECIO DE SU LLAMADA-----------------")
print("------------------------------------------------------")

#Input
tiempo = int(input("Ingrese la duracion de la llamada: "))

#processing
valor = 300 + 50*(tiempo-3) 
if tiempo <= 3:
    msj = "Su valor de la llamada es de: $300"
if tiempo > 3:
    msj = "Su valor de la llamada es de: $" + str(valor)

#Output
print(msj)