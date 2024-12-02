
#44. Realiza un programa que recorra todos los números comprendidos de 0 a 100 realizando saltos de 3 en 3. El resultado debe aparecer por pantalla en una línea con los números separados por ‘,’.


var_numeros = []
for contador in range(0, 101, 3):
    var_numeros.append(str(contador)) 
var_result = ','.join(var_numeros)
print(var_result)









