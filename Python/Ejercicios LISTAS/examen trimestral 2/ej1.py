#1
lista0=[]
lista1=[]
lista2=[]
numeros=""
maximo=0
minimo=0
promedio=0


numeros=input("Introduce...:")

lista0=numeros.split("-")
print(lista0)

lista1=[int(x) for x in lista0]

maximo=max(lista1)
minimo=min(lista1)
promedio=round(sum(lista1) / len(lista1),4)

for recorrer in lista1:
    if recorrer>promedio:
        lista2.append(recorrer)

print(maximo)
print(minimo)
print(promedio)
print(lista2)