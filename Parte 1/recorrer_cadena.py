"""
Este programa toma una frase ingresada por el usuario y convierte cada carácter a mayúsculas.

- Iteración sobre cadenas con un bucle for.
- Manipulación de cadenas con el método upper().
"""

def run():
    frase = input('Escribe una frase: ')
    for caracter in frase:  # Itera sobre cada carácter de la frase
        print(caracter.upper())  # Convierte el carácter a mayúscula y lo imprime

if __name__ == "__main__":
    run()
