"""
Este programa evalúa si una persona es mayor de edad utilizando una función y pruebas unitarias con `unittest`.

Conceptos básicos en Python:
- Uso de funciones con `return`
- Comparaciones lógicas (`>=`)
- Implementación de pruebas unitarias con `unittest`
- Métodos de aserción (`assertEqual`) para validar resultados esperados
"""

import unittest

def is_adult(age):
    """Returns True if the age is 18 or older, False otherwise."""
    return age >= 18  # Simplification of the condition

class CrystalTest(unittest.TestCase):
    """Set of tests to validate the `is_adult` function."""

    def test_is_adult(self):
        age = 20
        result = is_adult(age)
        self.assertEqual(result, True)  # Checks if it returns True

    def test_is_minor(self):
        age = 15
        result = is_adult(age)
        self.assertEqual(result, False)  # Checks if it returns False

if __name__ == "__main__":
    unittest.main()
