"""
Este programa verifica si un número es primo .
Un numero es primo cuando el residuo de la divicion es 0 solo cuando se divide entre uno,
y entre el mismo numero.

Conceptos básicos de Python que se aplican:

- Importación de módulos (math para operaciones matemáticas).
- Funciones y su retorno de valores.
- Uso de bucles e instrucciones de control (for, if, continue).
- Entrada de usuario con  input() y conversión de tipos.
"""

import math

def is_prime_number(number):
    square_root = int(math.sqrt(number))  # Calculates the square root and converts it to an integer
    counter = 0

    for i in range(1, square_root + 1):
        if i == 1 or i == number:  # Skips 1 and the number itself
            continue
        if number % i == 0:  # Checks if it is divisible
            counter += 1

    return counter != 1  # Returns True if it is prime, False otherwise

def run():
    number = int(input('Enter the number you want: '))  # Asks the user for a number
    if is_prime_number(number):
        print('The number is prime')
    else:
        print('The number is not prime')

if __name__ == "__main__":
    run()
