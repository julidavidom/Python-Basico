"""
Este programa encuentra la raíz cuadrada de un número usando aproximaciones sucesivas.
Si el número no tiene una raíz exacta, se devuelve una aproximación con un margen de error (epsilon).

Conceptos básicos en Python:
- Entrada de datos con `input()`
- Uso de `while` para iteraciones con condición
- Operaciones con números de punto flotante
- Control de errores con margen de tolerancia (`epsilon`)
"""

def find_square_root(target, epsilon=0.01):
    step = epsilon**2
    answer = 0.0

    while abs(answer**2 - target) >= epsilon and answer <= target:
        answer += step
        print(f"Diferencia: {abs(answer**2 - target)}, Aprox: {answer}")

    if abs(answer**2 - target) >= epsilon:
        print(f"No se encontró la raíz cuadrada de {target}")
    else:
        print(f"La raíz cuadrada de {target} es aproximadamente {answer}")

if __name__ == '__main__':
    number = int(input('Escoge un número: '))
    find_square_root(number)