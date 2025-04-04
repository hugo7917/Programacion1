
#37. Programa que pregunte cuantas notas quiero introducir y para cada nota diga si estoy aprobado o suspendido.

var_numeros= int(input("introduce el numero de notas que quieras: "))

for contador in range (var_numeros):
    var_nota=float(input("Introduce tu primera nota: "))
    if var_nota>5:
        print("Enhorabuena, has aprobado")
    if var_nota<5:
        print("Lo sineto, has suspendido")
