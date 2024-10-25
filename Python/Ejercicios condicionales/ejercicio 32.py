
#32. Cómo solucionarías con ayuda de métodos String el problema del ejercicio anterior para no distinguir entre mayúsculas y minúsculas.

txt= ("A quien madruga dios la ayuda")

var_1=input("introduce una palabra: ")

txt_2=txt.lower()
var_1_2= var_1.lower()

if var_1_2 in txt_2:
    var_2=txt_2.find(var_1_2)
    print("la plabra esta en la frase y esta en el indice: ", var_2)
else:
    print("la plabra no esta en la frase")















