
#20: A partir del ejercicio anterior, forzar que el usuario solo pueda introducir por teclados nomeros entre 1 y 10

var_1=int(input("introduce un numero: "))
var_2=int(input("introduce otro numero: "))



if var_1>var_2:
    print("El numero",var_1," es mayor que" ,var_2,)
    
if var_1<var_2:
    print("El numero",var_2," es mayor que" ,var_1,)
    
if var_1==var_2:
    print("El numero",var_1," es igual que" ,var_2,)


if var_1>10:
    print("hay numero fuera de los limites")

if var_1<0:
    print("hay numero fuera de los limites")

if var_2>10:
    print("hay numero fuera de los limites")

if var_2<0:
    print("hay numero fuera de los limites")
