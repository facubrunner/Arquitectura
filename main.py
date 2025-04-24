from random import sample

# Números ganadores (ruleta)
ruleta = sample(range(0, 46), 6)

# Registro de jugadores
jugadores = {}
cantidad_jugadores = 3

# Pedir números a cada jugador
for jugador in range(1, cantidad_jugadores + 1):
    print("\nJugador", jugador)
    numeros = []

    while len(numeros) < 6:
        try:
            n = int(input("Elegí un número entre 0 y 45: "))
            if n < 0 or n > 45:
                print("Debe estar entre 0 y 45.")
            elif n in numeros:
                print("Ya elegiste ese número.")
            else:
                numeros.append(n)
        except ValueError:
            print("Solo se aceptan números.")

    jugadores[f"Jugador {jugador}"] = numeros

# Mostrar resultados
print("\n--- RESULTADO DEL SORTEO ---")
print("Números ganadores:", ruleta)

for nombre, numeros in jugadores.items():
    aciertos = [n for n in numeros if n in ruleta]
    print("\n", nombre)
    print("Números elegidos:", numeros)
    print("Aciertos:", aciertos)
    print("Cantidad de aciertos:", len(aciertos))