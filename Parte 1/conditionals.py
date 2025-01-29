"""
Programa que evalúa si un número ingresado por el usuario es mayor, menor o igual a 5.
Este ejemplo introduce la estructura condicional if-elif-else en Python.
"""

# Solicitar un número al usuario
numero = int(input('Escribe un número: '))

# Evaluar el número ingresado
if numero > 5:
    print('Es mayor a 5')
elif numero == 5:
    print('Es igual a 5')
else:
    print('Es menor a 5')
