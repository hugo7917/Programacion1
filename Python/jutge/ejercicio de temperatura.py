temperatura = int(input("Introduce la temperatura en grados Celsius: "))

if temperatura > 30:
    print("Hace calor")
elif temperatura < 10:
    print("Hace frío")
else:
    print("Está bien")

if temperatura >= 100:
    print("El agua herviría")
elif temperatura <= 0:
    print("El agua se congelaría")

