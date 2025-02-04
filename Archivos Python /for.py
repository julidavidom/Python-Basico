"""
Ejemplo de uso de bucles en Python: while y for.
Se muestra cómo iterar con while, cómo usar range() en for y cómo generar listas con range().
"""

# Example with while
counter = 1
while counter < 1000:
    print(counter)
    counter += 1  # Optimized way to increment

# Example with for using range()
for counter in range(1000):
    print(counter)

# Generate a list with range()
number_list = list(range(1000))
print(number_list)

# Multiplication table of 11 using for
for i in range(10):
    print(11 * i)