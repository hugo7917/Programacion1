#14. Realiza un programa que a partir de introducir el diámetro de un círculo calcule el área y perímetro. Importa la librería match y utiliza el valor PI para hacer el cálculo. Redondea el resultado a un decimal.
import math
var1=int(input("dime el diametro de un circulo: "))
var_pi=math.pi
print("el area del circulo es: ", round(((var1/2)**2)*var_pi,1))
print("el perimetro del circulo es: ", round(2*var_pi*(var1/2),1))
