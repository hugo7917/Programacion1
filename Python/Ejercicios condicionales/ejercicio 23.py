
#23. Modifica el programa anterior para establecer si la nota es un excelente (8.5 a 10), un notable (>=6.5 -<8.5), satisfactorio (<6.5 -5) o insuficiente (<5). Controla que la nota introducida esté entre 0 y 10. Utilizar elif sin operadores lógicos.

var_1=float(input("dime la nota de tu examen: "))

if var_1>10.0:
    print("la nota esta fuera de los limites")

elif var_1<0.0:
    print("la nota esta fuera de los limites")

elif var_1==0:
    print("has sacado un insuficiente")

elif var_1<5:
    print("has sacado un insuficiente")

elif var_1==5:
    print("has sacado un suficiente")

elif var_1<6.5:
    print("has sacado un suficiente")

elif var_1==6.5:
    print("has sacado un notable")

elif var_1<8.5:
    print("has sacado un notable")

elif var_1==8.5:
    print("has sacado un excelente")

elif var_1<10:
    print("has sacado un excelente")

elif var_1==10:
    print("has sacado un excelente")








