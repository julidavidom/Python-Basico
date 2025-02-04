"""
Este programa implementa el método de Enumeración Exhaustiva para encontrar la raíz cuadrada exacta de un número entero.

Conceptos básicos en Python:
- Uso de variables y entrada de usuario (`input`, `int`)
- Bucle `while` para iteración controlada
- Condicionales `if-else` para verificar resultados
"""

# Request an integer from the user
target = int(input("Choose an integer: "))
answer = 0

# Find the exact square root using incremental addition
while answer**2 < target:
    answer += 1

# Check if the number has an exact square root
if answer**2 == target:
    print(f"The square root of {target} is {answer}")
else:
    print(f"{target} does not have an exact square root")