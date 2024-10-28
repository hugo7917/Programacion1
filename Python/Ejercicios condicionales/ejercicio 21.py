
#21. Programa que calcula una ecuación de segundo grado. Controla que el valor de la raíz cuadrada no de un valor negativo

import math

var_1=int(input("introduce el primer valor: "))
var_2=int(input("introduce el seegundo valor: "))
var_3=int(input("introduce el tercer valor: "))

var_raiz=(var_2**2)-(4*var_1*var_3)

if var_raiz>0:
    var_resultado1=(((-var_2)+math.sqrt(var_raiz))/2*var_1)
    var_resultado2=(((-var_2)-math.sqrt(var_raiz))/2*var_1)
    print("el valor del primer resultado es: ",var_resultado1)
    print("el valor del segundo resultado es: ",var_resultado2)

else:
    print("la raiz no puede ser negativa")


