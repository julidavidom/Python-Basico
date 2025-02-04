"""
Programa que evalúa si un número ingresado por el usuario es mayor, menor o igual a 5.
Este ejemplo introduce la estructura condicional if-elif-else en Python.
"""

# Request a number from the user
number = int(input('Enter a number: '))

# Evaluate the entered number
if number > 5:
    print('It is greater than 5')
elif number == 5:
    print('It is equal to 5')
else:
    print('It is less than 5')