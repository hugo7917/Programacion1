#47. Realiza un programa donde el usuario introduzca por teclado 2 intervalos, por pantalla se debe mostrar el rango de números teniendo en cuenta que se a<b la secuencia será incremental y si a>b la secuencia en descenso. Respeta el formato de salida

var_a = int(input("Introduce el primer intervalo: "))
var_b = int(input("Introduce el segundo intervalo: "))

rango = ""

if var_a < var_b:
    for i in range(var_a, var_b + 1):
        rango += str(i)  
        if i != var_b:  
            rango += "-"
else:
    for i in range(var_a, var_b - 1, -1):
        rango += str(i)  
        if i != var_b:  
            rango += "-"
print(rango)
