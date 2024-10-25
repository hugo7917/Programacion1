#30. Realiza un programa que controle si la longitud de una frase introducida por teclado es igual, menor o mayor de 11 caracteres. Utiliza elif.


var_1= input("dime una frase: ")

if (len(var_1))>11:
    print("la frase tiene mas de 11 caracteres")

elif (len(var_1))==11:
    print("la frase tiene 11 caracteres")

elif (len(var_1))<11:
    print("la frase tiene menos de 11 caracteres")



