import random

# Función que genera una contraseña aleatoria de 15 caracteres
def generar_contrasena():
    # Listas de caracteres posibles para la contraseña
    mayusculas = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    simbolos = ['!', '#', '$', '&', '/', '(', ')']
    numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    # Combina todas las listas de caracteres en una sola
    caracteres = mayusculas + minusculas + simbolos + numeros

    # Lista para almacenar los caracteres de la contraseña
    contrasena = []

    # Genera 15 caracteres aleatorios
    for i in range(15):
        caracter_random = random.choice(caracteres)  # Escoge un carácter al azar
        contrasena.append(caracter_random)  # Añade el carácter a la lista

    # Une los caracteres en una cadena y la devuelve
    contrasena = "".join(contrasena)
    return contrasena


def run():
    contrasena = generar_contrasena()  # Llama a la función que genera la contraseña
    print('Tu nueva contraseña es: ' + contrasena)  # Muestra la contraseña generada

# Ejecuta la función 'run' solo si este archivo es ejecutado directamente
if __name__ == '__main__':
    run()
