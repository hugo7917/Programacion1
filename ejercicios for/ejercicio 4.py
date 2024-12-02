
#38. A partir del programa anterior, establece los rangos para que el usuario no pueda introducir notas inferiores a 0 y superiores a 10

var_numeros= int(input("introduce el numero de notas que quieras: "))

for contador in range (var_numeros):
    var_nota=float(input("Introduce tu primera nota: "))
    if var_nota<0 or var_nota>10:
        print("Eror, vuelve a intentarlo")
    else:
        if var_nota>5:
            print("Enhorabuena, has aprobado")
        if var_nota<5:
            print("Lo sineto, has suspendido")









