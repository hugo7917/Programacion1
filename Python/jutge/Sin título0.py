#ejemplo jutge

concatenar=""
palabras=input()
lista=palabras.split()
for recorrer in lista:
    concatenar=recorrer + " " + concatenar

print(concatenar[:-1]