#70. Crea un programa que permita introducir x palabras en una lista llamada lista1. Una vez introducidas, crea una nueva lista, llamada lista2, exactamente igual a lista1. Se deben mostrar por pantalla el contenidos de lista1 en orden ascendente y lista2 en orden descendente. Respeta el formato de entrada y salida tal y como se muestra en el testeo.

numero=0
milista=[]
milista2=[]
var_cantidad=0

var_cantidad=int(input("introduce una cantidad palabras:"))

for recorre in range(o,var_cantidad):
    numero=(input("introduce una palabra: "))
    milista.append(numero)

milista.sort()
print(milista)

milista_2=milista
milista_2.reverse()
print(milista_2)

