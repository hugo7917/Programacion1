
#31. Asigna a una variable de texto la siguiente frase: A quién madruga Dios ayuda. Comprueba si existen las siguientes palabras mostrando por pantalla la posición de su índice.

txt= ("A quien madruga dios la ayuda")

var_1=input("introduce una palabra: ")

if var_1 in txt:
    var_2=txt.find(var_1)
    print("la plabra esta en la frase y esta en el indice: ", var_2)
else:
    print("la plabra no esta en la frase")





