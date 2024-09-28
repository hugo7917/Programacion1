#15. Utiliza el valor Pi de la librería math para calcular el área y volumen de un cilindro, introduciendo por teclado el valor de radio y altura. Resultado con 2 decimales.


import math
var_pi=math.pi
var1=int(input("dime el valor del radio de un cilindro: "))
var2=int(input("dime el valor de la altura de un cilindro"))
print("el area del cilindro es: ", round(2*var_pi*var1*(var2+var1),2))
print("el volumen del cilindro es: ", round(var_pi*(var1**2)*var2,2)) 
