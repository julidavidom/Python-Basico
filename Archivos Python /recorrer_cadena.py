"""
Este programa toma una frase ingresada por el usuario y convierte cada carácter a mayúsculas.

- Iteración sobre cadenas con un bucle for.
- Manipulación de cadenas con el método upper().
"""

def run():
    sentence = input('Enter a sentence: ')
    for character in sentence:  # Iterates over each character in the sentence
        print(character.upper())  # Converts the character to uppercase and prints it

if __name__ == "__main__":
    run()

