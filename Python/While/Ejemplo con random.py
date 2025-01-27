<<<<<<< HEAD
#EJEMPLO RANDOM

import random
numero=0
numero_secreto=random.randint(1,5)

while numero != numero_secreto:
    numero=int(input("Introduce el numero secreto entre el 1 y el 5: "))    
    if numero != numero_secreto:
        print("gilipollas, esta mal")
    if numero==numero_secreto:
=======
#EJEMPLO RANDOM

import random
numero=0
numero_secreto=random.randint(1,10)

while numero_secreto != numero:
    numero=int(input("Introduce el numero secreto entre el 1 y el 10: "))    
    if numero_secreto != numero:
        print("gilipollas, esta mal")
    if numero==numero_secreto:
>>>>>>> b1e0f5e5dbf9d2ff07982fe395969f12be400cf0
        print("Está bien")