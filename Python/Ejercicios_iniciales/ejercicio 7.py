#7. programa que calcule dos operandos con los 7 operadores vistos en clase. ¿Cómo puedes forzar que el resultado de la división tenga 2 decimales?

var1=float(input("dame un valor: "))
var2=float(input("dame un segundo valor: "))
print=(f"la suma de (var1) + (var2) es: ", var1 + var2)
print=(f"la resta de (var1) - (var2) es: ", var1 - var2)
print=(f"el producto de (var1) * (var2) es: ", var1 * var2)
print=(f"la división de (var1) / (var2) es: ", round(var1 / var2, 2))
print=(f"la potencia de (var1) elevado a (var2) es: ", var1**var2)
print=(f"la división entera de (var1) // (var2) es: ", var1 / var2)
