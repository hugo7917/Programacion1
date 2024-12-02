
#39. Programa que pida n números y que, tras introducir el último número, debe aparecer por pantalla el número total de positivos, negativos y número de 0.


var_total_numeros=int(input("introduce la cantidad de numeros que deseas introducir: "))
var_numero_0=0
var_numero_pos=var_numero_0
var_numero_neg=0
for contador in range(var_total_numeros):
    var_numero=float(input("introduce tu numero: "))
   
    if var_numero>0:
        var_numero_pos=var_numero_pos+1
    if var_numero<0:
        var_numero_neg=var_numero_neg+1
    if var_numero==0:
        var_numero_0=var_numero_0+1
print("El total de números positivos es: ", var_numero_pos)
print("El total de números negativos es: ", var_numero_neg)
print("El total de ceros es: ", var_numero_0)


