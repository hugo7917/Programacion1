#2
frase2=""
frase=input("Introduce...:")
lista1=frase.split()
palabra=input("Introduce palabra...:")
contar=lista1.count(palabra)

for recorrer in lista1:
    frase2=frase2 + recorrer +  ","

print(contar)
print(frase2[:-1])



