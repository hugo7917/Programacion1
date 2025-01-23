#56. Realiza un programa que gestione un establecimiento de venta de bocadillos. Un pedido se compone de: bocadillo, acompañamiento y bebida. Un cliente puede pedir más de un pedido. El dependiente a partir del menú (ver imagen), se encarga de introducir los datos. El menú solo se visualiza una vez al ejecutar el programa. El programa debe preguntar al dependiente tras la realización de un pedido, si quiere gestionar otro.

print("MENÚ")
print("1M. Bocadillo de calamares- 9 €")
print("2M. Bocadillo de chistorra - 4.5 €")
print("3M. Bikini de jamón - 2.5 €")
print("ACOMPAÑAMIENTO")
print("1A. Patatas finas - 1.5 €")
print("2A. Patatas gruesas - 1.75 €")
print("3A. Patatas rústicas - 2 €")
print("BEBIDAS")
print("1B. Coca cola - 2 €")
print("2B. Acuarius - 1.5 €")
print("3B. Agua - 1 €")

var_menú=int(input("Escoge un menu: "))
var_acompañamiento=int(input("Escoge un acompañamiento: "))
var_bebidas=int(input("Escoge una bebida: "))

1M= 9
2M= 4.5
3M= 2.5
1A= 1.5
2A= 1.75
3A= 2
1B= 2
2B= 1.5
3B= 1

print ("El valor tital a pagar es de: ", (var_menú + var_acompañamiento + var_bebidas))





