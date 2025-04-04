#46. A partir del programa anterior, soluciona el error que se produce en el test anterior con la palabra Abrigo utilizando únicamente una instrucción.



palabra = input("Introduce una palabra: ")

vocales = "aeiouáéíóúüAEIOUÁÉÍÓÚÜ"

lista_vocales = ""
lista_consonantes = ""

for letra in palabra:
    if letra.isalpha():  
        if letra in vocales:
            lista_vocales += letra
        else:
            lista_consonantes += letra

print(f"Las vocales de la palabra {palabra} son: {lista_vocales}")
print(f"Las consonantes de la palabra {palabra} son: {lista_consonantes}")
