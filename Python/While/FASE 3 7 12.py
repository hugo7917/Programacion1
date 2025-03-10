# FASE 3 7 1/2

import random

valores_cartas = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 10: 0.5, 11: 0.5, 12: 0.5}
Alias = input("Escribe tu alias: ")
def mostrar_puntuacion(puntuacion):
    print(f"{Alias}, tu puntuación actual es de: {puntuacion:.1f}")

def jugar():
    print(f"{Alias}, bienvenido al juego del 7 y medio!")
    
    while True:
        puntuacion_jugador = 0
        continuar = "si"

        while puntuacion_jugador < 7.5 and continuar.lower() == "si":
            carta = random.choice([1, 2, 3, 4, 5, 6, 7, 10, 11, 12])
            valor_carta = valores_cartas[carta]
            
            print(f"\nLa carta es: {carta} (valor: {valor_carta:.1f})")
            puntuacion_jugador += valor_carta
            mostrar_puntuacion(puntuacion_jugador)

            if puntuacion_jugador < 7.5:
                continuar = input(f"¿Quieres otra carta {Alias}? (si/no): ")

        if puntuacion_jugador == 7.5:
            print(f"\n¡Enhorabuena {Alias}, has ganado la partida! ¡Estás en racha, vuelve a probar y quizá volverás a ganar!")
        elif puntuacion_jugador > 7.5:
            print(f"\n¡Has perdido la partida {Alias}! Te has pasado de 7.5. ¡Vuelve a probar y quizá esta vez ganes!")
        elif puntuacion_jugador >= 6:
            print(f"\nTe has plantado {Alias}. ¡Has sabido plantarte a tiempo!")
        else:
            print(f"\nTe has plantado {Alias}. Quizás tendrías que arriesgar un poco, ¿no? ¡Quien no arriesga no gana!")

        jugar




