#58. Modifica el programa anterior para que tengas 3 intentos. Utiliza while

import random
numero=0
numero_secreto=random.randint(1,5)

while numero != numero_secreto:
    numero=int(input("Introduce el numero secreto entre el 1 y el 5: "))    
    if numero != numero_secreto:
        print("Está mal")
    if numero==numero_secreto:
        print("Está bien")
















