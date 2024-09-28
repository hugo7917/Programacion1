#16. Utiliza el método sqrt de la librería math para calcular la raíz cuadrada de un número. El resultado de la raíz cuadrada divídelo entre 2 de manera que se obtenga siempre un resultado entero. Haz que se muestre por pantalla los dos  resultados de todo el proceso (raíz y división).

import math
var_raizcuadrada=math.sqrt
var1=(int(input("dime un valor: ")))
print("la raiz cuadrada es: ", round(var_raizcuadrada(var1),1))
print("la raiz cuadrada entre dos es: ", round((var_raizcuadrada(var1))/2,0))
