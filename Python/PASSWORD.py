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

password=input("introduce una contraseña de entre 6 y 8 caracteres:")
        
if len(password)==8 or len(password)==7 or len(password)==6:
    if password[0]<str(1) or password[0]>str(5) :
        print("El error esta en el caracter 1")
    
    if password[1].islower()== False:
        print("El error esta en el carcter 2")

    if password[2].isupper()== False:
        print("El error esta en el carcter 3")

    if password[3] not in "*_@":
        print("El error esta en el carcter 4")
        
    if password[4].islower()== False:
        print("El error esta en el carcter 5")

    if password[5]<str(6) or password[5]>str(9) :
        print("El error esta en el caracter 6")

    elif len(password)==7 or len(password)==8:
        if password[6] not in ["&","/","#"]:
            print("El error esta en el carcter 7")            

    elif len(password)==8:
        if password[7]>str(5) or password[7]==(5) :
            print("El error esta en el caracter 8")

if len(password)<6: 
    print("La contraseña no llega al numero de caracteres necesarios")
    
if len(password)>8:
    print("La contraseña supera el numero de carcteres permitidos")
    
    
    #print("La contraseña cumple los requsitos")






