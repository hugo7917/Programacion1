#EJEMPLO RANDOM

import random
numero=0
numero_secreto=random.randint(1,10)

while numero_secreto != numero:
    numero=int(input("Introduce el numero secreto entre el 1 y el 10: "))    
    if numero_secreto != numero:
        print("gilipollas, esta mal")
    if numero==numero_secreto:
        print("Está bien")