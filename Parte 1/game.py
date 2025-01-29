"""
Este programa es un simple juego de adivinanza en el que el usuario debe
adivinar un número aleatorio generado por el programa.

Conceptos básicos de Python aplicados:

- Uso del módulo random para generar números aleatorios.
- Entrada de usuario con input() y conversión a entero.
- Uso de estructuras condicionales if-else.
- Bucle while para repetir la interacción hasta acertar.
"""

import random

def run():
    numero_aleatorio = random.randint(1, 100)  # Genera un número aleatorio entre 1 y 100
    numero_elegido = int(input('Elige un número del 1 al 100: '))

    while numero_aleatorio != numero_elegido:  # Se repite hasta que el usuario acierte
        if numero_elegido < numero_aleatorio:
            print('Elige un número más grande')
        else:
            print('Elige un número más pequeño')

        numero_elegido = int(input('Elige otro número: '))  # Nueva entrada del usuario

    print("¡Ganaste!")  # Mensaje de éxito cuando el número es adivinado

if __name__ == "__main__":
    run()
