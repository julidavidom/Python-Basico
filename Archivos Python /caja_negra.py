"""
Este programa implementa una función para sumar dos números y la valida mediante pruebas unitarias con `unittest`.

Conceptos básicos en Python:
- Definición y uso de funciones (`def`)
- Operaciones aritméticas (`+`)
- Implementación de pruebas unitarias (`unittest`)
- Métodos de aserción (`assertEqual`) para verificar resultados esperados
"""

import unittest

def add(num_1, num_2):
    """Returns the sum of two numbers."""
    return num_1 + num_2

class BlackBoxTest(unittest.TestCase):
    """Unit tests for the `add` function."""

    def test_add_two_positives(self):
        """Checks the sum of two positive numbers."""
        result = add(10, 5)
        self.assertEqual(result, 15)

    def test_add_two_negatives(self):
        """Checks the sum of two negative numbers."""
        result = add(-10, -7)
        self.assertEqual(result, -17)

if __name__ == "__main__":
    unittest.main()

