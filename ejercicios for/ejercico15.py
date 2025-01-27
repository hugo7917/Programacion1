#49. A partir del programa anterior, modifica el código para que al introducir la letra por teclado te indique en qué posición de la palabra se encuentra la letra.


var_palabra_secreta = input("Introduce la palabra secreta: ").lower()

var_oportunidades = len(var_palabra_secreta)

for _ in range(var_oportunidades):
    var_letra = input("Introduce una letra: ").lower()  
    
    if var_letra in var_palabra_secreta:
        var_posiciones = [i + 1 for i in range(len(var_palabra_secreta)) if var_palabra_secreta[i] == var_letra]
        for var_posición in var_posiciones:
            print(f"la letra se encuentra en la posición {var_posición}")
    else:
        print("la letra no existe")
