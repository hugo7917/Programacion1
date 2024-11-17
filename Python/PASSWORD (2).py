#Realitzar un programa que permeti introduir una ‘paraula clau’ amb unes carcteristiques.

print("Estas son las reglas de el password:")
print("posición 1. Un numero mayor o igual a 1 y menor o igual que 5. ")
print("posición 2. Una letra minuscula. ")
print("posición 3. Una letra mayuscula. ")
print("posición 4. Uno de los siguientes simbolos: *, _, @. ")
print("posición 5. Una letra minuscula. ")
print("posición 6. Un numero mayor o igual a 6 y menor o igual que 9. ")
print("posición 7. Uno de los siguientes simbolos: &, /, #. ")
print("posición 8. Un numero menor o igual que 5. ")

#En las proximas dos lineas pido la contraseña y creo una variable que contara el numero de errores de la contraseña para que al final se le informe al que introduce la contraseña si está o no bien hecha la contraseña.
password=input("introduce una contraseña de entre 6 y 8 caracteres:")
var_errores_totales=0

#Aqui comienzo poniendo una condición la cual determina que el numero de caracteres maximo para la contraseña son 8 y el minimo son 6.
if len(password)==8 or len(password)==7 or len(password)==6:
    
    if password[0]<str(1) or password[0]>str(5):
        print("El error esta en el caracter 1", end=" ")
        var_errores_totales=var_errores_totales+1
        
    if password[1].islower()==False:
        print("El error esta en el caracter 2", end=" ")
        var_errores_totales=var_errores_totales+1
        
    if password[2].isupper()==False:
        print("El error esta en el caracter 3", end=" ")
        var_errores_totales=var_errores_totales+1
        
    if password[3] not in ["*", "_", "@"]:
        print("El error esta en el caracter 4", end=" ")
        var_errores_totales=var_errores_totales +1
        
    if password[4].islower()==False:
        print("El error esta en el caracter 5", end=" ")
        var_errores_totales=var_errores_totales +1
    
    if password[5]<str(6) or password[5]>str(9):
        print("El error esta en el caracter 6", end=" ")
        var_errores_totales=var_errores_totales+1
    if len(password)==6:
        if var_errores_totales==0:
            print("La contraseña cumple los requisitos")

    elif password[6] not in ["&", "/", "#"]:
        print("El error esta en el caracter 7", end=" ")
        var_errores_totales=var_errores_totales +1
    elif len(password)==7:
        if var_errores_totales==0:
            print("La contraseña cumple los requisitos")
            
    elif password[7]>str(5):
        print("El error esta en el caracter 8")  
        var_errores_totales=var_errores_totales +1
    else:
        if var_errores_totales==0:
            print("La contraseña cumple los requisitos")
#Aqui concreto que si la contraseña supera o no llega al numero de carcteres necesarios, tiene que saltar error
if len(password)<6: 
    print("La contraseña no llega al numero de caracteres necesarios")
    
if len(password)>8:
    print("La contraseña supera el numero de caracteres permitidos")
        
