"""
Programa que calcula y muestra las potencias de 2 hasta alcanzar un límite específico.
Este ejemplo introduce el uso del bucle 'while' y la manipulación de números en Python.
"""

def main():
    limite = 1000000
    contador = 0
    potencia_2 = 2 ** contador  # 2 elevado a la potencia del contador

    # Bucle while para calcular potencias de 2 hasta alcanzar el límite
    while potencia_2 < limite:
        print('2 elevado a ' + str(contador) + ' es igual a: ' + str(potencia_2))
        contador = contador + 1
        potencia_2 = 2 ** contador

if __name__ == '__main__':
    main()
