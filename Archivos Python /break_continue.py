"""
Este script demuestra el uso de estructuras de control en Python, 
como bucles `for`, `break` y `continue`.

El código imprime 'NA' 12 veces y luego 'HEY JUDE'.
Se incluyen ejemplos comentados de otros usos de `break` y `continue`.
"""

def run():
    # Loop that prints 'NA' 12 times and then 'HEY JUDE'
    for i in range(13):
        if i == 12:
            print('HEY JUDE')
            break  # Ends the loop when i is 12
        print('NA')

    # EXAMPLE 1: Print only even numbers up to 1000.
    # for counter in range(1000):
    #     if counter % 2 != 0:
    #         continue  # Skips odd numbers
    #     print(counter)

    # EXAMPLE 2: Stop the loop when the counter reaches 5678
    # for i in range(10000):
    #     print(i)
    #     if i == 5678:
    #         break  # Stops the loop execution

    # EXAMPLE 3: Read a text and print each letter until an 'o' is found
    # text = input('Enter a text: ')
    # for letter in text:
    #     if letter == 'o':
    #         break  # Ends when an 'o' is found
    #     print(letter)

if __name__ == '__main__':
    run()