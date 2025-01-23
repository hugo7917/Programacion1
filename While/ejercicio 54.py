#54. Modifica el programa anterior y haz que se repita el ciclo automáticamente hasta que el total de todas las sumas sea superior a 50, será entonces cuando el programa finalice. No hará falta preguntar si deseas repetir la operación. En cada operación aparece por pantalla la suma de la operación y su acumulado. Para aquellos de vosotros que os fijáis en los detalles, controlar que el mensaje del acumulado es singular o plural.. . Con While

repeticiones = "sí"
total_sumas = 0
contador_repeticiones = 0

while repeticiones.lower() == "sí":
    num_1 = int(input("Ingresa el primer número entero: "))
    num_2 = int(input("Ingresa el segundo número entero: "))  
    resultado = num_1 + num_2
    print(f"La suma de {num_1} y {num_2} es: {resultado}")
    
    total_sumas += resultado
    contador_repeticiones += 1
    
    repeticiones = input("¿Deseas repetir la operación? (sí/no): ")

print(f"Total de las sumas: {total_sumas}")
print(f"Número de repeticiones: {contador_repeticiones}")
print("Gracias por usar el programa.") 




