
#36. Programa que sume los n primeros números naturales. n Lo introduce el usuario.


var_numeros= int(input("Intruduce un numero natural: "))
var_suma=0
for contador in range (var_numeros+1):
    var_suma= contador + var_suma
print(var_suma)




