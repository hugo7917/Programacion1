
#10. Introduce por teclado dos números y muestre por pantalla la siguiente información: cociente, resto y si el dividendo es par o impar. 
var1=float(input("dime un numer: "))
var2=float(input("dime otro numero: "))
print("El coeficiente es:", round(var1/var2, 2))
print("El dividendo es:", round(var1**var2, 2))
if var1%2==0:
    print("es par")
if not var1%2==0:
    print("es impar")


