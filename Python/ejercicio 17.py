#17. Calcula el índice de masa corporal IMC de una persona, introduciendo por teclado el peso (en kg) y dividiendo por la estatura (en metros y elevado al cuadrado). Si el resultado es igual o superior a 25, debe aparecer un mensaje informando de sobrepeso.

var1=float(input("dime el peso de una persona: "))
var2=float(input("dime la altura en metros de la misma persona: "))
var3=(var1/(var2**2))
print("el indice de mas acorporal de esta persona es: ", round(var3,2))
if var3>=25:
    print("esa persona tiene sobrepeso")
else:
    print("esapersona NO tiene sobrepeso")
