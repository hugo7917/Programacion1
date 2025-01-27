
# FOR CONTADOER IN RANGE:

var=0
total=0

var_min=int(input("Introduce un valor mínimo: "))
var_max=int(input("Introduce un valor máximo: "))

for contador in range (var_min,var_max, 2):
    total= total+contador
print(total)


# FOR CONTADOR IN STRING:
var="buenos días"
#etsa variable se utiliza para contar el numero de vueltas del for
contar=0

for recorrer in var:
    print(recorrer)
    contar+=1
print(contar)



var="b1enos d23s"
var_num=0
var_letras=0

for contador in(0,len(var)):
    if var[contador].isnumeric():
        var_num+=1
    if var[contador].isalpha():
        var_letras+=1
print("el total de letras es: ", var_letras)
print("el total de numeros es: ", var_num)
        



