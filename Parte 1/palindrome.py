# Función que verifica si una palabra o frase es un palíndromo
def palindromo(palabra):
    palabra = palabra.replace(' ', '')  # Elimina espacios
    palabra = palabra.lower()  # Convierte todo a minúsculas
    palabra_invertida = palabra[::-1]  # Invierte la cadena

    return palabra == palabra_invertida  # Retorna True si es palíndromo, False si no

# Función principal que solicita una palabra y verifica si es palíndromo
def run():
    palabra = input('Escribe una palabra: ')
    if palindromo(palabra):
        print('Es palíndromo')
    else:
        print('No es palíndromo')


if __name__ == '__main__':
    run()
