#73. Diseña un programa que compruebe si los valores de la lista1 (casa,mesa,sal,sol,agua) están repetidos o no en la lista2 (casa,luz,tres,tren,sol,pan). Haz que permita visualizar que palabras se repiten y cuales no

lista1 = ["casa", "mesa", "sal", "sol", "agua"]
lista2 = ["casa", "luz", "tres", "tren", "sol", "pan"]

repetidos = []
no_repetidos = []

for palabra in lista1:
    if palabra in lista2:
        repetidos.append(palabra)
    else:
        no_repetidos.append(palabra)

print("Palabras que se repiten:", repetidos)
print("Palabras que no se repiten:", no_repetidos)