#56. Realiza un programa que gestione un establecimiento de venta de bocadillos. Un pedido se compone de: bocadillo, acompañamiento y bebida. Un cliente puede pedir más de un pedido. El dependiente a partir del menú (ver imagen), se encarga de introducir los datos. El menú solo se visualiza una vez al ejecutar el programa. El programa debe preguntar al dependiente tras la realización de un pedido, si quiere gestionar otro.

bocadillos = [
    ("Bocadillo de calamares", 9),
    ("Bocadillo de chistorra", 4.5),
    ("Bikini de jamón", 2.5),]

acompañamientos = [
    ("Patatas finas", 1.5),
    ("Patatas gruesas", 1.75),
    ("Patatas rusticas", 2)]

bebidas = [
    ("Coca cola", 2),
    ("Acuarius", 1.5),
    ("Agua", 1)]

def mostrar_menu():
    print("--- Menú ---")
    
    print("Bocadillos:")
    i = 1
    for nombre, precio in bocadillos:
        print(f"{i}. {nombre} - ${precio:.2f}")
        i += 1
    
    print("Acompañamientos:")
    i = 1
    for nombre, precio in acompañamientos:
        print(f"{i}. {nombre} - ${precio:.2f}")
        i += 1
        
    print("Bebidas:")
    i = 1
    for nombre, precio in bebidas:
        print(f"{i}. {nombre} - ${precio:.2f}")
        i += 1

def realizar_pedido():
    total = 0

    seleccion_bocadillo = int(input("Seleccione un bocadillo (1-3): ")) - 1
    total += bocadillos[seleccion_bocadillo][1]

    seleccion_acompañamiento = int(input("Seleccione un acompañamiento (1-3): ")) - 1
    total += acompañamientos[seleccion_acompañamiento][1]

    seleccion_bebida = int(input("Seleccione una bebida (1-3): ")) - 1
    total += bebidas[seleccion_bebida][1]

    print(f"Total del pedido: ${total:.2f}")
    return total

def gestionar_pedidos():
    total_general = 0
    continuar = "si"
    
    while continuar.lower() == "si":
        mostrar_menu()
        total_pedido = realizar_pedido()
        total_general += total_pedido
        
        continuar = input("\n¿Quiere hacer otro pedido? (si/no): ")
    
    print(f"Total a pagar por todos los pedidos: ${total_general:.2f}")
    print("¡Gracias por su compra!")

if __name__ == "__main__":
    gestionar_pedidos()