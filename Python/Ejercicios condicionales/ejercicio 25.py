
#25. Repite el programa número 23 pero en esta ocasión utilizando operadores lógicos.


var_1=float(input("dime la nota de tu examen: "))

if var_1>10.0 or var_1<0.0:
    print("la nota esta fuera de los limites")

elif var_1==0 or var_1<5:
    print("has sacado un insuficiente")
    
elif var_1==5 or var_1<6.5:
    print("has sacado un suficiente")
    
elif var_1==6.5 or var_1<8.5:
    print("has sacado un notable")
    
elif var_1==8.5 or var_1<10 and var_1==10:
    print("has sacado un excelente")



