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
    random_number = random.randint(1, 100)  # Generates a random number between 1 and 100
    chosen_number = int(input('Choose a number from 1 to 100: '))

    while random_number != chosen_number:  # Repeats until the user guesses correctly
        if chosen_number < random_number:
            print('Choose a bigger number')
        else:
            print('Choose a smaller number')

        chosen_number = int(input('Choose another number: '))  # New user input

    print("You won!")  # Success message when the number is guessed

if __name__ == "__main__":
    run()

