<<<<<<< HEAD
#52. Realiza un programa que sume dos números enteros por teclado y presente el resultado por pantalla. El programa preguntará si deseas o no repetir la operación. Con While

repeticiones = "sí"
while repeticiones.lower() == "sí":
    num_1 = int(input("Ingresa el primer número entero: "))
    num_2 = int(input("Ingresa el segundo número entero: "))  
    resultado = num_1 + num_2
    print(f"La suma de {num_1} y {num_2} es: {resultado}")
    
    repeticiones = input("¿Deseas repetir la operación? (sí/no): ")

print("Gracias por usar el programa.")
