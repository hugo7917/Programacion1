letra = input()

if letra.isupper():
    caso = "Mayúscula"
else:
    caso = "Minúscula"

vocales = "aeiouAEIOU"  
if letra in vocales:
    vocal_o_consonante = "Vocal"
else:
    vocal_o_consonante = "Consonante"

print(f"La letra es {caso} y es una {vocal_o_consonante}.")

