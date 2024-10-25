#28. Mejora el programa anterior para controlar también la introducción de símbolos. Utiliza elif.


var_1= (input("dime una letra: "))

if var_1.islower()== True: 
    print("el valor es minuscula")

elif var_1.isnumeric()== True:
    print("El valor introducido es un numero")

elif var_1.isupper()== True:
    print("el valor es mayuscula")

else:
    print("el valor introducido es un simbolo")







