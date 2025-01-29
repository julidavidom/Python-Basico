"""
Ejemplo de uso de bucles en Python: while y for.
Se muestra cómo iterar con while, cómo usar range() en for y cómo generar listas con range().
"""

# Ejemplo con while
contador = 1
while contador < 1000:
    print(contador)
    contador += 1  # Forma optimizada de incrementar

# Ejemplo con for usando range()
for contador in range(1000):
    print(contador)

# Generar una lista con range()
lista_numeros = list(range(1000))
print(lista_numeros)

# Tabla del 11 usando for
for i in range(10):
    print(11 * i)
