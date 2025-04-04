horas = int(input("Horas: "))
minutos = int(input("Minutos: "))
segundos = int(input("Segundos: "))

segundos += 1

if segundos == 60:
    segundos = 0
    minutos += 1
    if minutos == 60:
        minutos = 0
        horas += 1
        if horas == 24:
            horas = 0
print(f"{horas:02d}:{minutos:02d}:{segundos:02d}")

