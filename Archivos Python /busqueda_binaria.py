"""
Este programa calcula la raíz cuadrada de un número utilizando el método de búsqueda binaria.
Si la raíz no es exacta, devuelve una aproximación con un margen de error (`epsilon`).

Conceptos básicos en Python:
- Entrada de datos con `input()`
- Uso de `while` para iteraciones con condición
- Implementación de búsqueda binaria para encontrar valores aproximados
- Manejo de números flotantes y precisión (`epsilon`)
"""

def find_binary_root(target, epsilon=0.01):
    low = 0.0
    high = max(1.0, target)  # Ensures a valid range even for values less than 1
    answer = (high + low) / 2  # Initial midpoint

    while abs(answer**2 - target) >= epsilon:
        print(f'Low: {low}, High: {high}, Approx: {answer}')

        if answer**2 < target:
            low = answer  # Adjust the lower bound
        else:
            high = answer  # Adjust the upper bound

        answer = (high + low) / 2  # Recalculate the midpoint
    print(f'The square root of {target} is approximately {answer}')

if __name__ == '__main__':
    number = int(input('Choose a number: '))
    find_binary_root(number)
