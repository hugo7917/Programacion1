
letra = input()

if letra.isupper():
    tipo_caso = "Mayúscula"
elif letra.islower():
    tipo_caso = "Minúscula"
else:
    tipo_caso = "No es una letra"

vocales = "aeiouAEIOU"
if letra.isalpha():  
    if letra in vocales:
        tipo_letra = "Vocal"
    else:
        tipo_letra = "Consonante"
else:
    tipo_letra = "Carácter inválido"

print(f"La letra es {tipo_caso} y es una {tipo_letra}.")


