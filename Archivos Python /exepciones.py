"""
Manejo de excepciones en Python con `try-except`.

Conceptos básicos abordados:
- Uso de listas y comprensión de listas (`list comprehension`)
- Manejo de excepciones con `try-except`
- `ZeroDivisionError` para evitar errores de división entre cero
"""

def divide_list_elements(lst, divisor):
    try:
        return [i / divisor for i in lst]  # Divide each element of the list
    except ZeroDivisionError as error:
        print(f"Error: {error}")  # Error message if the divisor is 0
        return lst  # Returns the original list unchanged

# Usage example
lst = list(range(10))  # List from 0 to 9
divisor = 0  # Error case (division by zero)
print(divide_list_elements(lst, divisor))
