#Ejemplo de LISTAS

milista=[]

numero=int(input("introduce un numero: "))

while numero!=0:
    milista.append(numero)
    numero=int(input("introduce un numero o 0 para acabar: "))
    
print(max(milista))
print(min(milista))

for recorrer in milista:
    total=total+recorrer
print(total)


for recorrer in range(0, len(milista)):
    total_1=total_1+milista[recorrer]
print(total_1)


for recorrer in milista:
    multi=reocrrer*2
    listamultiplicar.append(multi)


variable=sum(milista) 
print(variable)

