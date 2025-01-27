#58. Modifica el programa anterior para que tengas 3 intentos. Utiliza while

import random

numero_secreto = random.randint(1, 5)

intentos = 0
max_intentos = 3
numero = 0

while numero != numero_secreto and intentos < max_intentos:
    numero = int(input("Introduce el número secreto entre 1 y 5: "))
    intentos += 1  
    
    if numero != numero_secreto:
        print(f"Está mal. Te quedan {max_intentos - intentos} intentos.")
    else:
        print("¡Está bien! Has adivinado el número secreto.")
        break  

if numero != numero_secreto:
    print(f"Se acabaron los intentos. El número secreto era {numero_secreto}.")












