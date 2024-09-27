#12. Realiza un programa que, introduciendo en los valores de lado, base menor, base mayor y altura de un trapecio isósceles, nos devuelva por pantalla en el área y el perímetro.

var1=int(input("dime el valor de la base menor de un trapecio isosceles: "))
var2=int(input("dime el valor de la base mayor de un trapecio isosceles: "))
var3=int(input("dime el valor de la altura de un trapecio isosceles: "))
var4=int(input("dimne el valor de los lados de un trapecio isosceles: "))
print("el perimetro es: ", var1+var2+var4)
print("el area es: ", ((var1+var2)/2)*var3)
