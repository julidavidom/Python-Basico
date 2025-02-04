"""
Programa que calcula y muestra las potencias de 2 hasta alcanzar un límite específico.
Este ejemplo introduce el uso del bucle 'while' y la manipulación de números en Python.
"""

def main():
    limit = 1000000
    counter = 0
    power_of_2 = 2 ** counter  # 2 raised to the power of the counter

    # While loop to calculate powers of 2 until the limit is reached
    while power_of_2 < limit:
        print('2 raised to ' + str(counter) + ' is equal to: ' + str(power_of_2))
        counter = counter + 1
        power_of_2 = 2 ** counter

if __name__ == '__main__':
    main()
