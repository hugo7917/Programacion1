entrada = input("Escribe dos palabras separadas por un espacio: ")
palabra1, palabra2 = entrada.split()

if palabra1 < palabra2:
    print(f"{palabra1} < {palabra2}")
elif palabra1 > palabra2:
    print(f"{palabra1} > {palabra2}")
else:
    print(f"{palabra1} = {palabra2}")

