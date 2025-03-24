import random

# Diccionario de cartas y sus valores
valores_cartas = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 10: 0.5, 11: 0.5, 12: 0.5}

# Función para mostrar la puntuación
def mostrar_puntuacion(puntuacion, quien):
    print(f"{quien} tu puntuación actual es de: {puntuacion:.1f}")

# Función para que el jugador juegue su turno
def turno_jugador(alias):
    puntuacion_jugador = 0
    continuar = "si"
    
    while puntuacion_jugador < 7.5 and continuar.lower() == "si":
        carta = random.choice(list(valores_cartas.keys()))
        valor_carta = valores_cartas[carta]
        
        print(f"\nLa carta es: {carta} (valor: {valor_carta:.1f})")
        puntuacion_jugador += valor_carta
        mostrar_puntuacion(puntuacion_jugador, alias)
        
        if puntuacion_jugador == 7.5:
            print(f"\n¡{alias} ha alcanzado 7.5 y gana automáticamente!")
            return puntuacion_jugador, True
        
        if puntuacion_jugador < 7.5:
            continuar = input(f"¿Quieres otra carta {alias}? (si/no): ")
    
    return puntuacion_jugador, False

# Función para que la banca juegue su turno
def turno_banca(puntuacion_jugador):
    puntuacion_banca = 0
    
    while puntuacion_banca < 7.5:
        if puntuacion_banca >= puntuacion_jugador:
            break  # La banca se detiene si ya está ganando
        
        carta = random.choice(list(valores_cartas.keys()))
        valor_carta = valores_cartas[carta]
        
        print(f"\nLa Banca ha sacado la carta: {carta} (valor: {valor_carta:.1f})")
        puntuacion_banca += valor_carta
        mostrar_puntuacion(puntuacion_banca, "Banca")
        
        if puntuacion_banca == 7.5:
            print("\n¡La Banca ha alcanzado 7.5 y gana automáticamente!")
            return puntuacion_banca, True
        
        if puntuacion_banca > 7.5:
            break
    
    return puntuacion_banca, False

# Función principal del juego
def jugar():
    alias = input("Escribe tu alias: ")
    deposito = 100  # El jugador empieza con 100 puntos
    print(f"{alias} tienes un depósito inicial de {deposito} puntos.")
    
    while deposito > 0:
        print(f"\n{alias} tu depósito es de {deposito} puntos.")
        print(f"\n{alias}, bienvenido al juego del 7 y medio!")
        
        puntuacion_jugador, gana_automaticamente = turno_jugador(alias)
        
        if gana_automaticamente:
            deposito += 10
            continue
        
        if puntuacion_jugador > 7.5:
            print(f"\n¡Has perdido la partida {alias}! Te has pasado de 7.5. ¡Vuelve a probar y quizá esta vez ganes!")
            deposito -= 10
            continue
        
        print("\nEs el turno de la Banca...")
        input("Presiona Enter para que la Banca empiece a jugar...")
        
        puntuacion_banca, banca_gana_automaticamente = turno_banca(puntuacion_jugador)
        
        if banca_gana_automaticamente:
            deposito -= 10
            continue
        
        # Mostrar los resultados finales
        print(f"\nPuntuación final de {alias}: {puntuacion_jugador:.1f}")
        print(f"Puntuación final de la Banca: {puntuacion_banca:.1f}")
        
        # Condiciones para determinar el ganador
        if puntuacion_banca > 7.5:
            print(f"\nLa Banca ha superado 7.5. ¡{alias} gana!")
            deposito += 10
        elif puntuacion_jugador == puntuacion_banca:
            print("\n¡Empate!")
        elif puntuacion_jugador > puntuacion_banca:
            print(f"\n¡{alias} gana!")
            deposito += 10
        else:
            print("\nLa Banca gana!")
            deposito -= 10
        
        if deposito <= 0:
            print(f"\nTu depósito se ha agotado {alias}. Ya no puedes continuar jugando, ¡ahorra y vuelve cuando puedas!")
            break
        
        jugar_otra_vez = input(f"\n¿Quieres jugar otra vez {alias}? (si/no): ")
        if jugar_otra_vez.lower() != "si":
            break

if __name__ == "__main__":
    jugar()

