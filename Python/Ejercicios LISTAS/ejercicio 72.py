#72. A partir del ejercicio anterior, se da por hecho que las vocales con o sin acento son repetidas y no deben almacenarse en la lista

letras = []
vocales_con_acento = ['a', 'á', 'e', 'é', 'i', 'í', 'o', 'ó', 'u', 'ú']

while True:
    letra = input("Introduce una letra: ").lower()  

    if letra in vocales_con_acento:
        letra = 'vocal'

    if letra not in letras:
        letras.append(letra)
    else:
        print("La letra ya ha sido introducida anteriormente.")

    repetir = input("¿Deseas repetir? s/n: ").lower()

    if repetir != 's':
        break  

print("Las letras introducidas son:", letras)