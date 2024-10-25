#27. Mejora el programa anterior para controlar que el valor introducido es una letra y en caso de introducir un número, aparezca un aviso por pantalla.

var_1= (input("dime una letra: "))

if var_1.islower()== True: 
    print("el valor es minuscula")

elif var_1.isnumeric()== True:
    print("El valor introducido es un numero")

elif var_1.isupper()== True:
    print("el valor es mayuscula")

else:
    print("la letra es mayuscula ¿?")









