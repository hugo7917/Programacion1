#FASE 3 7 1/2

import random

# Diccionario de cartas y sus valores
valores_cartas = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 10: 0.5, 11: 0.5, 12: 0.5}

# Solicitar el alias del jugador
Alias = input("Escribe tu alias: ")

# Función para mostrar la puntuación
def mostrar_puntuacion(puntuacion, quien):
    print(f"{Alias} tu puntuación actual es de: {puntuacion:.1f}")

# Función para que el jugador juegue su turno
def turno_jugador():
    puntuacion_jugador = 0
    continuar = "si"
    
    while puntuacion_jugador < 7.5 and continuar.lower() == "si":
        carta = random.choice([1, 2, 3, 4, 5, 6, 7, 10, 11, 12])
        valor_carta = valores_cartas[carta]
        
        print(f"\nLa carta es: {carta} (valor: {valor_carta:.1f})")
        puntuacion_jugador += valor_carta
        mostrar_puntuacion(puntuacion_jugador, Alias)
        
        if puntuacion_jugador < 7.5:
            continuar = input(f"¿Quieres otra carta {Alias}? (si/no): ")
    
    return puntuacion_jugador

# Función para que la banca juegue su turno
def turno_banca():
    puntuacion_banca = 0
    while puntuacion_banca < 5.0:  # La banca pide cartas hasta obtener al menos 5
        carta = random.choice([1, 2, 3, 4, 5, 6, 7, 10, 11, 12])
        valor_carta = valores_cartas[carta]
        
        print(f"\nLa Banca ha sacado la carta: {carta} (valor: {valor_carta:.1f})")
        puntuacion_banca += valor_carta
        mostrar_puntuacion(puntuacion_banca, "Banca")
    
    while puntuacion_banca < 7.5:  # La banca sigue pidiendo cartas hasta llegar a 7.5 o más
        carta = random.choice([1, 2, 3, 4, 5, 6, 7, 10, 11, 12])
        valor_carta = valores_cartas[carta]
        
        print(f"\nLa Banca ha sacado la carta: {carta} (valor: {valor_carta:.1f})")
        puntuacion_banca += valor_carta
        mostrar_puntuacion(puntuacion_banca, "Banca")
        
        if puntuacion_banca > 7.5:
            break
    
    return puntuacion_banca

# Función principal del juego
def jugar():
    deposito = 100  # El jugador empieza con 100 puntos
    print(f"{Alias} tienes un depósito inicial de {deposito} puntos.")
    
    while deposito > 0:
        print(f"\n{Alias} tu depósito es de {deposito} puntos.")
        print(f"\n{Alias}, bienvenido al juego del 7 y medio!")
        
        puntuacion_jugador = turno_jugador()  # El jugador juega su turno
        
        if puntuacion_jugador > 7.5:
            print(f"\n¡Has perdido la partida {Alias}! Te has pasado de 7.5. ¡Vuelve a probar y quizá esta vez ganes!")
            deposito -= 10
            continue
        
        print("\nEs el turno de la Banca...")
        input("Presiona Enter para que la Banca empiece a jugar...")
        
        puntuacion_banca = turno_banca()  # La banca juega su turno
        
        # Mostrar los resultados finales
        print(f"\nPuntuación final de {Alias}: {puntuacion_jugador:.1f}")
        print(f"Puntuación final de la Banca: {puntuacion_banca:.1f}")
        
        # Condiciones para determinar el ganador
        if puntuacion_banca > 7.5:
            print(f"\nLa Banca ha superado 7.5. ¡{Alias} gana!")
            deposito += 10
            
        elif puntuacion_jugador == puntuacion_banca:
            print("\n¡Empate!")
        elif puntuacion_jugador > puntuacion_banca:
            print(f"\n¡{Alias} gana!")
            deposito += 10
        else:
            print("\nLa Banca gana!")
            deposito -= 10
        
        # Comprobar si el jugador puede seguir jugando
        if deposito <= 0:
            print(f"\nTu depósito se ha agotado {Alias}. Ya no puedes continuar jugando, ¡ahorra y vuelve cuando puedas!")
            break
        
        # Preguntar si el jugador quiere jugar otra vez
        jugar_otra_vez = input(f"\n¿Quieres jugar otra vez {Alias}? (si/no): ")
        if jugar_otra_vez.lower() != "si":
            break

if __name__ == "__main__":
    jugar()
