#Realitzar un programa que permeti introduir una ‘paraula clau’ amb unes carcteristiques.

print("INSTRUCCIONES: La longitud del password debe ser de 8 caracteres, debe tener 1 letra mayúscula, 2 minúsculas, 3 números entre 1-5, y 2 símbolos de estos: /, *, #, @")

for i in range(3):
    print(f"\nIntroduce la contraseña {i + 1}:")
    password = input("Contraseña: ")

    var_error1 = "Falta una letra en mayúscula."
    var_error2 = "Faltan dos letras minúsculas."
    var_error3 = "Faltan tres números entre 1-5."
    var_error4 = "Faltan 2 símbolos de estos: /, #, @."
    var_errores_totales = var_error1 + " " + var_error2 + " " + var_error3 + " " + var_error4

    var_ind = 0
    var_mayusculas = 0
    var_minusculas = 0
    var_num1_5 = 0
    var_simbolos = 0
    var_len = len(password)

    for var_ind in range(var_len):  
        if password[var_ind].isupper():
            var_mayusculas += 1
        elif password[var_ind].islower():
            var_minusculas += 1
        elif password[var_ind].isnumeric() and 1 <= int(password[var_ind]) <= 5:
            var_num1_5 += 1
        elif password[var_ind] in "/#@*":
            var_simbolos += 1

    if var_mayusculas >= 1 and var_minusculas >= 2 and var_num1_5 >= 3 and var_simbolos >= 2 and var_len == 8:
        print(f"La contraseña {i + 1} es válida.")
    else:
        print(f"La contraseña {i + 1} es inválida.")
