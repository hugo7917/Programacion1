

var1=float(input("dime un numer: "))
var2=float(input("dime otro numero: "))
print("El coeficiente es:", round(var1/var2, 2))
print("El dividendo es:", round(var1**var2, 2))
if var1%2==0:
    print("es par")
if not var1%2==0:
    print("es impar")


