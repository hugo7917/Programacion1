#80. Utilizando listas, crea un programa que te permita determinar si un número es decimal o no. 

lista=[]
lista2=[]

numero=input("Introduce un núimero: ")

lista=numero.split(".")

if len(lista)!=2:
    print("no es decimal")
else:
    if lista[0].isnumeric() and lista[1].isnumeric:
        print("esd ecimal")
    else:
        print("no es decimal")

print(lista)

