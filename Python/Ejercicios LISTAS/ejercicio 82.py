# 82. Modifica el programa anterior para que sea el usuario intente adivinar la palabra escogida al azar de la lista, indicando si es correcto o no. El programa debe no finaliza hasta que no se adivine la palabra

import random  

lista = ["casa", "barco", "gato", "perro", "madera", "agua", "puente", "pantalón"]  
palabra_secreta = random.choice(lista)

while True:
    intento = input("Adivina la palabra: ").strip().lower()
    if intento == palabra_secreta:
        print("¡Correcto! Has adivinado la palabra.")
        break
    else:
        print("Incorrecto, intenta de nuevo.")


