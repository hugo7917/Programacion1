# FASE 3 7 1/2

import random

tipos_cartas = random.randint(1,7)

valores_cartas = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7,10: 0.5, 11: 0.5, 12: 0.5}

def mostrar_puntuacion(puntuacion):
    print(f"Puntuación actual: {puntuacion:.1f}")

def jugar():
    deposito = 100  
    print(f"Tienes un depósito inicial de {deposito} puntos.")
    
    while deposito > 0:
        print(f"\nTu depósito tiene {deposito} puntos.")
        print("Bienvenido al juego del 7 y medio!")

        puntuacion_jugador = 0
        continuar = "si"

        while puntuacion_jugador < 7.5 and continuar.lower() == "si":
            carta = random.choice([1, 2, 3, 4, 5, 6, 7, 10, 11, 12])
            valor_carta = valores_cartas[carta]
            
            print(f"\nLa carta es: {carta} (valor: {valor_carta:.1f})")
            puntuacion_jugador += valor_carta
            mostrar_puntuacion(puntuacion_jugador)
#Esta parte del program he decidido cambiarla un poco más para que el programa no sea tan seco y no parezca que te está 
#hablando una maquina y así, de paso, incito al jugador a que vuelva a jugar con algunas frases.
            if puntuacion_jugador < 7.5:
                continuar = input("¿Quieres otra carta? (si/no): ")
        
        if puntuacion_jugador == 7.5:
            print("\n¡Enhorabuena, has ganado la partida! ¡Estas en racha, vuelve a probar y quizá vuelvas a ganar!")
            deposito += 10
        elif puntuacion_jugador > 7.5:
            print("\n¡Has perdido la partida! Te has pasado de 7.5.¡Vuelve a proba y quizá esta vez ganes!")
            deposito -= 10
        elif puntuacion_jugador >= 6:
            print("\nTe has plantado. ¡Has sabido plantarte a tiempo!.")
            deposito += 5
        else:
            print("\nTe has plantado. Quizás tendrías que arriesgar un poco ¿no?, ya que ¡Quien no arriesga no gana!")
            deposito -= 5
        
        if deposito <= 0:
            print("\nTu depósito se ha agotado. Ya no puedes continuar jugando, ¡ahorra y vuelve cuando puedas!.")
            break
        
        jugar_otra_vez = input("\n¿Quieres jugar otra vez? (si/no): ")
        if jugar_otra_vez.lower() != "si":
            break

if __name__ == "__main__":
    jugar()




