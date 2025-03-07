#74. A partir del programa anterior, haz que se visualicen tanto las palabras que se repiten o no de entre las 2 listas.

lista1 = ["casa", "mesa", "sal", "sol", "agua"]
lista2 = ["casa", "luz", "tres", "tren", "sol", "pan"]

set_lista1 = set(lista1)
set_lista2 = set(lista2)

repetidos_en_lista1 = set_lista1.intersection(set_lista2)
repetidos_en_lista2 = set_lista2.intersection(set_lista1)

no_repetidos_en_lista1 = set_lista1.difference(set_lista2)
no_repetidos_en_lista2 = set_lista2.difference(set_lista1)

print("Palabras repetidas en lista1 que están en lista2:", repetidos_en_lista1)
print("Palabras repetidas en lista2 que están en lista1:", repetidos_en_lista2)
print("Palabras no repetidas en lista1:", no_repetidos_en_lista1)
print("Palabras no repetidas en lista2:", no_repetidos_en_lista2)