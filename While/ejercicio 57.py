#57. Realiza un programa que permita adivinar un número comprendido entre 1 y 5. El programa debe controlar si el usuario introduce un número no comprendido entre 1 y 5

import random
numero=0
numero_secreto=random.randint(1,5)

while numero != numero_secreto:
    numero=int(input("Introduce el numero secreto entre el 1 y el 5: "))    
    if numero != numero_secreto:
        print("gilipollas, esta mal")
    if numero==numero_secreto:
        print("Está bien")












