#18. Cines Paradiso celebran su décimo aniversario y por ser un día especial realizan importantes descuentos. A los adultos se les aplicará un 10% de descuento y a los menores de 18 años un 50%. Si la entrada cuesta 12 euros, calcula el total a pagar introduciendo por teclado el número de menores y el número de adultos que asisten al cine.

var1=int(input("dime el numero demenores que asistiran a la actuación: "))
var2=int(input("dime el numero de adultos que asistiran a la actuación: "))
var3=((var1*12)/2)
var4=(((var2*12)/10)*9)
print("El precio total del cine para los menores es de: ", round(var3,1))
print("El precio total del cine para los adultos es de: ", round(var4,1))
