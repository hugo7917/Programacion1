#Ejemplo LISTA 2

frase=input("introduce una frase")

milista=frase.split(",")
print(milista[2])

palabra=input("introduce la palabra que quieras contar: ")
print(milista.count(palabra))