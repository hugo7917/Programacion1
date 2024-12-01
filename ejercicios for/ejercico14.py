#48. Realiza un programa que introduzcas por teclado una palabra ‘secreta’, consigue la longitud de esa palabra para que sea ese el criterio que establezca el rango del bucle de manera que el usuario tenga x oportunidades para ver si letra introducida está en esa palabra.

var_palabra_secreta = input("Introduce la palabra secreta: ").lower()

var_oportunidades = len(var_palabra_secreta)

for _ in range(var_oportunidades):
    letra = input("Introduce una letra: ").lower()  
    if letra in var_palabra_secreta:
        print("la letra existe")
    else:
        print("la letra no existe")
