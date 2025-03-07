#75. Crea una lista con el siguiente nombre lista1 y su contenido: a,b,D,x,r,X,3,h,w,2,i. Presenta por pantalla los siguientes resultados:
#a. Cantidad total de valores
#b. Cantidad de números
#c. Cantidad de letras
#d. Cantidad de mayúsculas
#e. Suma de los valores numéricos

lista1 = ['a', 'b', 'D', 'x', 'r', 'X', 3, 'h', 'w', 2, 'i']

total_valores = len(lista1)
cantidad_numeros = 0
cantidad_letras = 0
cantidad_mayusculas = 0
suma_numeros = 0

for item in lista1:
    if isinstance(item, int):  
        cantidad_numeros += 1
        suma_numeros += item
    elif isinstance(item, str): 
        cantidad_letras += 1
        if item.isupper():  
            cantidad_mayusculas += 1

print(f"a. Cantidad total de valores: {total_valores}")
print(f"b. Cantidad de números: {cantidad_numeros}")
print(f"c. Cantidad de letras: {cantidad_letras}")
print(f"d. Cantidad de mayúsculas: {cantidad_mayusculas}")
print(f"e. Suma de los valores numéricos: {suma_numeros}")

