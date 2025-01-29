"""
Este programa verifica si un número es primo .
Un numero es primo cuando el residuo de la divicion es 0 solo cuando se divide entre uno,
y entre el mismo numero.

Conceptos básicos de Python que se aplican:

- Importación de módulos (math para operaciones matemáticas).
- Funciones y su retorno de valores.
- Uso de bucles e instrucciones de control (for, if, continue).
- Entrada de usuario con input() y conversión de tipos.
"""

import math

def el_numero_es_primo(numero):
    raiz_del_num = int(math.sqrt(numero))  # Calcula la raíz cuadrada y la convierte en entero
    contador = 0

    for i in range(1, raiz_del_num + 1):
        if i == 1 or i == numero:  # Omite 1 y el mismo número
            continue
        if numero % i == 0:  # Verifica si es divisible
            contador += 1

    return contador != 1  # Devuelve True si es primo, False si no

def run():
    numero = int(input('Escribe el número que deseas: '))  # Solicita un número al usuario
    if el_numero_es_primo(numero):
        print('El número es primo')
    else:
        print('El número no es primo')

if __name__ == "__main__":
    run()
