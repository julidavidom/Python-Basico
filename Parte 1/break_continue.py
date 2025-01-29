"""
Este script demuestra el uso de estructuras de control en Python, 
como bucles `for`, `break` y `continue`.

El código imprime 'NA' 12 veces y luego 'HEY JUDE'.
Se incluyen ejemplos comentados de otros usos de `break` y `continue`.
"""

def run():
    # Bucle que imprime 'NA' 12 veces y luego 'HEY JUDE'
    for i in range(13):
        if i == 12:
            print('HEY JUDE')
            break  # Termina el bucle cuando i es 12
        print('NA')

    # EJEMPLO 1: Imprimir solo los números pares hasta 1000.
    # for contador in range(1000):
    #     if contador % 2 != 0:
    #         continue  # Salta los números impares
    #     print(contador)

    # EJEMPLO 2: Detener el bucle cuando el contador llega a 5678
    # for i in range(10000):
    #     print(i)
    #     if i == 5678:
    #         break  # Detiene la ejecución del bucle

    # EJEMPLO 3: Leer un texto e imprimir cada letra hasta encontrar una 'o'
    # texto = input('Escribe un texto: ')
    # for letra in texto:
    #     if letra == 'o':
    #         break  # Termina cuando encuentra una 'o'
    #     print(letra)

if __name__ == '__main__':
    run()