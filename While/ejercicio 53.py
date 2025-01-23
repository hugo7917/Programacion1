#53. A partir del código anterior, haz que aparezca al finalizar el programa por pantalla el total las sumas y el número de repeticiones. Con While

repeticiones = "sí"
total_sumas = 0

while repeticiones.lower() == "sí":
    num_1 = int(input("Ingresa el primer número entero: "))
    num_2 = int(input("Ingresa el segundo número entero: "))  
    resultado = num_1 + num_2
    print(f"La suma de {num_1} y {num_2} es: {resultado}")
    
    total_sumas += resultado 
    repeticiones = input("¿Deseas repetir la operación? (sí/no): ")

print(f"Total de las sumas: {total_sumas}")
print("Gracias por usar el programa.") 





















