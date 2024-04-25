#1. ingresar numero de jugadores
#2. pedir el nombre a los jugadores
#3. escribir un numero mayor a 15000 realizar el juegp
#4. sacar un numero random de 1 hasta el numero que se dijito en el numeral 3
#5. reasignar al ramdom el numero numero que se salio para ir reduciendo la cantidad de ramdoms
#6. el que saque el numero 1 pierde

import random

# Función para obtener un número válido mayor a 15000
def obtener_numero_valido():
    """Esta funcion es para validad que se ingrese un numero mayor a 15000
    """
    while True:
        try:
            numero = int(input("Ingresa un número mayor a 15000: "))
            if numero > 15000:
                return numero
            else:
                print("El número debe ser mayor a 15000. Intenta nuevamente.")
        except ValueError:
            print("Por favor, ingresa un número válido.")

# Función para jugar el juego con intercalación de jugadores
def jugar_juego(numero_maximo, jugadores):
    jugador_actual = 0  # Índice del jugador actual en la lista de jugadores

    while numero_maximo > 1:
        if int(input("1. continuar: ")) == 1:
            numero_random = random.randint(1, numero_maximo)
            print(f"{jugadores[jugador_actual]} #: {numero_random} \n")

            if numero_random == 1:
                jugador_perdido = jugadores.pop(jugador_actual)
                print(f"{jugador_perdido} sacó el número 1 y ha sido eliminado del juego.")
                return

            if numero_random == 2:
                jugador_perdido = jugadores.pop((jugador_actual + 1) % len(jugadores))
                print(f"{jugador_perdido} sacó el número 1 y ha sido eliminado del juego.")

            numero_maximo = numero_random - 1

        # Cambiar al siguiente jugador
        jugador_actual = (jugador_actual + 1) % len(jugadores)

# Obtener nombres de los jugadores
jugadores = []
num_jugadores = int(input("Ingrese el número de jugadores: "))

for i in range(num_jugadores):
    nombre = input(f"Ingrese el nombre del Jugador {i + 1}: ")
    jugadores.append(nombre)

while len(jugadores) > 1:
    # Obtener un número válido para el juego
    numero_juego = obtener_numero_valido()

    print("Comienza el juego...")
    jugar_juego(numero_juego, jugadores)

if len(jugadores) == 1:
    print(f"{jugadores[0]} es el ganador final del juego.")
