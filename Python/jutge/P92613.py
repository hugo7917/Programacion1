import math

x = float(input("Introduce un número real mayor o igual que 0: "))

if x >= 0:
    piso = math.floor(x)
    techo = math.ceil(x)
    redondeado = round(x)

    print(f"Parte entera hacia abajo (floor): {piso}")
    print(f"Parte entera hacia arriba (ceiling): {techo}")
    print(f"Redondeado: {redondeado}")
else:
    print("Error: el número debe ser mayor o igual que 0.")

