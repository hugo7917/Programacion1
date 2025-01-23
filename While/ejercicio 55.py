#55. Última vez que reutilizamos el mismo código.. lo prometo . A partir del programa anterior haz que sea todo exactamente igual pero teniendo en cuenta que el programa se repita siempre y cuando la suma acumulada sea superior a 50 o la suma acumulada sea par. Con While


total_sumas = 0
contador_repeticiones = 0

while total_sumas > 50 or total_sumas % 2 == 0:  
    num_1 = int(input("Ingresa el primer número entero: "))
    num_2 = int(input("Ingresa el segundo número entero: "))  
    resultado = num_1 + num_2
    total_sumas += resultado
    contador_repeticiones += 1
    
    print(f"La suma de {num_1} y {num_2} es: {resultado}")
    
    if total_sumas >= 50:
        break  

print(f"Total de las sumas: {total_sumas}")
print(f"Número de repeticiones: {contador_repeticiones}")
print("Gracias por usar el programa.")








