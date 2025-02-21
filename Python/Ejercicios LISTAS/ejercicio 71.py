#71. Haz un programa que permita al usuario introducir letras en una lista (cantidad indefinida), en esta lista no deben almacenarse las letras que se han introducido repetidas.

letras = []

while True:
    letra = input("Introduce una letra: ")
    
    if letra not in letras:
        letras.append(letra)
    else:
        print("La letra ya ha sido introducida anteriormente.")
    
    repetir = input("¿Deseas repetir s/n: ").lower()
    
    if repetir != 's':
        break  

print("Las letras introducidas son:", letras)