
### **Bienvenido a este repositorio. Aquí comparto conceptos básicos que he adquirido en programación con Python, estos ejemplos simples pueden ser de gran utilidad en algoritmos más complejos. El material lo he adquirido  a través de cursos virtuales, bootcamps y proyectos personales.**
---

# 🐍 PARTE 1 - Introducción al funcionamiento Python 🚀
Aquí aprenderás cómo funciona internamente este lenguaje interpretado, sus características clave y la diferencia entre lenguajes compilados e interpretados. Además, se incluyen códigos prácticos y explicaciones claras para que puedas comprender mejor cada concepto.

---
## 💻 1 ¿Qué es un lenguaje de programación? 
Un lenguaje de programación es un lenguaje formal que, mediante una serie de instrucciones, permite al programador escribir un conjunto de órdenes, acciones consecutivas, datos y algoritmos para crear programas que controlen el comportamiento físico y lógico de una máquina.

---
## 🧑‍💻 2 ¿Cómo Funciona Python?
Python es un lenguaje interpretado, lo que significa que el código no se traduce directamente a código de máquina como en los lenguajes compilados, sino que pasa por un proceso de interpretación que lo convierte en un formato intermedio (bytecode) que la máquina puede ejecutar.

### 📝 2.1 Lenguajes Compilados (Ejemplo: C++)
Los lenguajes compilados, como C++, convierten el código fuente a código de máquina directamente mediante un proceso de compilación. Este tipo de lenguajes suelen ser más rápidos en tiempo de ejecución.

```plaintext
C++ -----> compilador -----> código de máquina
```

### 🔄 2.2 Lenguajes Interpretados (Ejemplo: Python)
En Python, el código pasa por una máquina virtual que convierte el código a un formato intermedio (bytecode), y luego lo ejecuta. Esto hace que Python sea multiplataforma y fácil de usar en diferentes sistemas operativos.

```plaintext
Python -----> bytecode -----> máquina virtual de Python -----> ejecución
```
---
## 🧑‍🔧 3 Preguntas Frecuentes
### ⚡ 3.1 ¿Son los lenguajes interpretados más lentos?
En general, sí, pero la versatilidad y facilidad de uso de Python lo hacen ideal para muchas aplicaciones como análisis de datos, machine learning y desarrollo web. En muchos casos, la diferencia en velocidad no es un factor limitante.

### 🧹 3.2 ¿Qué es el Garbage Collector en Python?
Python incluye un recolector de basura que se encarga de liberar memoria automáticamente eliminando objetos no utilizados. Esto mejora la eficiencia y previene problemas de memoria.

### 🗂️ 3.3 ¿Qué es la carpeta pycache?
La carpeta pycache contiene el bytecode de los archivos Python, lo que optimiza la ejecución del código al evitar la recompilación innecesaria en ejecuciones futuras.

---
## 🏷️ 4 ¿Qué es un objeto? 
Un objeto es un concepto, abstracción o cosa con límites bien definidos que tiene un significado dentro del problema que se está manejando.

---
## 📁 5 Organización de los Archivos de tu Proyecto
Es esencial tener una buena organización en los proyectos Python, especialmente cuando crecen en tamaño y complejidad. Python organiza su código en módulos y paquetes.

### 📦 5.1 Módulos
Un módulo es cualquier archivo de Python .py que contiene código reutilizable. Ejemplos comunes incluyen math, random, y os.

### 📂 5.2 Paquetes
Un paquete es una carpeta que contiene módulos y debe incluir un archivo especial llamado init.py. Este archivo indica que la carpeta es un paquete de Python.

Ejemplo de estructura de proyecto:

```plaintext
Exploracion_espacial
    README.md            # Descripción del proyecto
    requirements.txt      # Librerías necesarias
    .gitignore            # Archivos ignorados por Git
    venv                  # Entorno virtual
    exploracion_espacial
        __init__.py
        nave.py
        destino.py
        plataforma.py
        lanzamiento.py
        test.py
        validacion.py
```
---

## 🔤 6 Tipado en Python
Python es un lenguaje dinámico, pero puedes utilizar anotaciones de tipado para mejorar la claridad de tu código.

### 📝 6.1 Tipado Estático vs Dinámico
En lenguajes estáticos como C++ o Java, debes especificar el tipo de cada variable.
En Python, puedes declarar variables sin un tipo específico, y el tipo se asignará dinámicamente durante la ejecución.

### 📏 6.2 Tipado Estático en Python
Aunque Python es dinámico, desde la versión 3.5, puedes usar anotaciones de tipado para hacer el código más legible y fácil de depurar.

```python
# Anotación de tipado para variables
a: int = 5
b: str = 'Hola'
c: bool = True
```
### 🧮 6.3 Funciones con Tipado Estático
Puedes añadir anotaciones de tipado a las funciones para definir qué tipo de datos aceptan y devuelven.

```python
def suma(a: int, b: int) -> int:
    return a + b
resultado = suma(3, 4)
print(resultado)
```
### 📊 6.4 Listas y Diccionarios con Tipado Estático
El módulo typing te permite declarar los tipados de los elementos en listas y diccionarios.

```python
from typing import List, Dict
# Lista de enteros
numeros: List[int] = [1, 2, 3, 4, 5]

# Diccionario con claves como cadenas y valores como enteros
usuarios: Dict[str, int] = {
    "argentina": 1,
    "mexico": 34,
    "colombia": 45
}
```
### 🔢 6.5 Tuplas con Tipado Estático
Las tuplas son colecciones inmutables que también pueden tener tipados definidos.

```python
from typing import Tuple

# Tupla con un entero, un flotante y un entero
valores: Tuple[int, float, int] = (1, 3.14, 5)
```

### 🔗 6.6 Tipados Complejos en Python
Puedes combinar diferentes tipados utilizando el módulo typing, lo que permite crear estructuras complejas como listas de diccionarios con tuplas.

```python
from typing import Dict, List, Tuple

# Lista de diccionarios, donde cada diccionario tiene como valor una tupla de enteros
coordenadas: List[Dict[str, Tuple[int, int]]] = [
    {"coord1": (1, 2), "coord2": (3, 5)},
    {"coord1": (0, 1), "coord2": (2, 5)}
]
```
---
## 🔨 7 Recomendación de Herramientas
Aunque Python es un lenguaje de tipado dinámico, puedes usar la herramienta mypy para realizar un análisis estático de los tipados en tu código. Esto es especialmente útil para asegurarte de que los tipados son correctos antes de ejecutar el código.

---
## 🚀 8 Ventajas del Tipado Estático
Claridad: Mejora la legibilidad del código.

- Prevención de errores: Detecta problemas antes de la ejecución.
- Colaboración: Facilita el trabajo en equipos de desarrollo grandes.
- Seguridad: Reduce la probabilidad de errores complejos que son difíciles de detectar en proyectos grandes.

---
# PARTE 2 - Guía de Conceptos de Programación 📚
En esta sección, encontrarás un recorrido completo por los conceptos esenciales de la programación en Python. Desde los tipos de datos y operaciones matemáticas hasta estructuras de control e iteraciones, este material está diseñado tanto para principiantes como para programadores que deseen reforzar sus conocimientos. Todos los códigos están comentados para facilitar su comprensión y aplicación en proyectos reales.

---
## 1 Tipos de datos básicos en programación 🧮
Los tipos de datos más comunes son:

- **int**: Números enteros.
- **float**: Números con decimales.
- **bool**: Valores booleanos (True o False).
- **str**: Cadenas de texto.

Ejemplo de definición de variables:
```python
my_int = 1
my_float = 1.0
my_bool = True
my_none = None
my_str = "Hola"
```
Imprimiendo el tipo de una variable:

```python
print(type(my_int))   # <class 'int'>
print(type(my_float)) # <class 'float'>
print(type(my_bool))  # <class 'bool'>
print(type(my_none))  # <class 'NoneType'>
print(type(my_str))   # <class 'str'>
```

---
## 2 Operaciones básicas en Python ➗
Operaciones matemáticas comunes:

```python
1 + 1      # Resultado: 2
2 - 5      # Resultado: -3
2.0 * 3    # Resultado: 6.0
6 // 2     # Resultado: 3
6 // 4     # Resultado: 1
6 / 4      # Resultado: 1.5
7 % 2      # Resultado: 1
2 ** 2     # Resultado: 4
```

---
## 3 Iteraciones en Python 🔁
Las iteraciones nos permiten repetir un proceso varias veces. Son fundamentales en la programación para realizar tareas repetitivas.

### 3.1 Puntos clave:
- Las iteraciones se pueden anidar (escribir iteraciones dentro de otras).
- **break** se utiliza para salir anticipadamente de una iteración.
- Hay que tener cuidado con iteraciones infinitas.

**Ejemplo**
```python
contador=0
while contador < 10:
    print(contador)
    contador = contador +1
```
---
## 4 Representación de números flotantes en Python 🏞️
La representación de números flotantes (tipo float) en Python y otras computadoras puede ser sorprendentemente inexacta debido a la forma en que se manejan internamente.

Ejemplo problemático:

```python
x = 0.0
for i in range(10):
    x += 0.1

if x == 1.0:
    print(f'x = {x}')
else:
    print(f'x != {x}')
```

Resultado esperado:

```python
x != 1.0
```

Aunque en teoría 0.1 * 10 = 1.0, al intentar representarlo en una computadora en base binaria, se obtiene una pequeña imprecisión: 0.999999999999.

**¿Por qué no se representan de manera exacta?**

En las computadoras, los números flotantes no se pueden representar con total precisión. Esto ocurre porque algunos valores, como 0.1, no tienen una representación exacta en binario debido a las limitaciones de la cantidad de dígitos significativos que pueden ser almacenados.

### 4.1 Representación binaria 🔢
- Cómo funciona: Los números se representan como secuencias de 0s y 1s en binario.
- El problema: Algunos números decimales no pueden ser representados exactamente en este formato.

**Ejemplos:**
- El número 0.625 tiene una representación exacta en binario: 101 * 2**-3.
- Sin embargo, 0.1 no puede representarse de forma precisa. En su lugar, se aproxima a un valor cercano, lo que genera un error de representación.

---
### 4.2 Precisión en Python 🐍
Python utiliza 53 bits de precisión para manejar números flotantes en la mayoría de las implementaciones modernas.
Esto significa que números como 0.1 son extremadamente cercanos a su valor real, pero nunca exactamente iguales.
Ejemplo de resultado inesperado:

```python
0.1000000000000000055511151231257827021181583404541015625
```

### 4.3 Buenas prácticas para trabajar con flotantes ✅
Debido a estas imprecisiones, no compares números flotantes con el operador ==. En su lugar, utiliza comparaciones aproximadas.

**Ejemplo:**

```python
abs(x - 1.0) < 1e-9  # Verifica si la diferencia es lo suficientemente pequeña
```
---
## 🔍5 Algoritmos de Búsqueda
### 5.1 Enumeración Exhaustiva 🕵️‍♂️
- También conocido como "adivina y verifica", este método enumera todas las posibilidades.
- Es uno de los primeros algoritmos que debes probar.

Ejemplo de código:

```python
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
```

### 5.2 Aproximación de Soluciones 📏
- Similar a la enumeración exhaustiva, pero no requiere una respuesta exacta.
- Podemos aproximar soluciones con un margen de error llamado epsilon.
- Epsilon es la diferencia entre la realidad y la solución. Cuanto más pequeño sea epsilon, más nos acercaremos a la solución, pero se requerirá más procesamiento.

Ejemplo de código:

```python
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
```

### 5.3 Búsqueda Binaria 🔎
- Requiere que el conjunto de números esté ordenado (ej. [1, 2, 3, 4, ...]).
- Es altamente eficiente, ya que reduce el espacio de búsqueda a la mitad en cada iteración.

Ejemplo de código:

```python
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
```

---
## 🛠 6 Funciones
### 6.1 Abstracción 🧠
No necesitas saber cómo se implementa algo, solo cómo manejarlo.

### 6.2 Descomposición 🧩
Permite dividir el código en componentes que colaboran entre sí. Piensa en mini programas que juntos forman un programa mayor.

### 6.3 Recursividad 🔄
- Definición algorítmica: Utiliza el enfoque "divide y vencerás". Encuentra una solución base y luego itera para resolver el problema.
- Definición programática: Una función que se llama a sí misma.

Ejemplo: Factoriales
```python
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
```
Ejemplo: Fibonacci

```python
def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
```

### 6.4 Funciones como Objetos 🎯
- En Python, las funciones son "ciudadanos de primera clase". Esto significa que:
- Tienen un tipo.
- Se pueden pasar como argumentos a otras funciones.
- Se pueden usar en expresiones.
- Se pueden incluir en estructuras de datos como listas, tuplas, diccionarios, etc.

Ejemplo: Pasar funciones como argumentos

```python
def multiply_by_two(n):
    return n * 2

def add_two(n):
    return n + 2

def apply_operation(f, numbers):
    results = []
    for number in numbers:
        results.append(f(number))
    return results

nums = [1, 2, 3]
print(apply_operation(multiply_by_two, nums))  # [2, 4, 6]
print(apply_operation(add_two, nums))  # [3, 4, 5]
```

Funciones Lambda

```python
add = lambda x, y: x + y
print(add(2, 3))  # 5
```

---
## 7 Tuplas 📦
Las tuplas son secuencias inmutables de objetos. Pueden contener cualquier tipo de objeto y se utilizan para devolver múltiples valores en una función.

Ejemplo:

```python
my_tuple = (1, 'dos', True)
print(my_tuple[0])  # 1

# Las tuplas son inmutables
# my_tuple[0] = 2  # TypeError

# Concatenación de tuplas
my_other_tuple = (2, 3, 4)
my_tuple += my_other_tuple
print(my_tuple)  # (1, 'dos', True, 2, 3, 4)
```

---
### 8 Rangos 🔢
Los rangos representan una secuencia de enteros. Son inmutables y muy eficientes en términos de memoria.

Ejemplo:

```python
my_range = range(0, 7, 2)
for i in my_range:
    print(i)  # 0, 2, 4, 6
```

---
## 9 Listas y Mutabilidad 📝
Las listas son secuencias de objetos mutables. Es importante tener cuidado con los efectos secundarios al modificar listas.

Ejemplo:

```python
my_list = [1, 2, 3, 4]
my_list.append(5)
print(my_list)  # [1, 2, 3, 4, 5]

# Clonación de listas
a = [1, 2, 3]
b = a[:]  # Clonar usando rebanadas
print(b)  # [1, 2, 3]
```
List Comprehension

```python
double = [i * 2 for i in range(10)]
print(double)  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
```

---
## 10 Diccionarios 📚
Los diccionarios son estructuras de datos que utilizan llaves en lugar de índices. Son mutables y no tienen un orden interno.

Ejemplo:

```python
my_dict = {'David': 35, 'Erika': 32, 'Jaime': 50}
print(my_dict['David'])  # 35

# Iterar sobre diccionarios
for key, value in my_dict.items():
    print(key, value)
```

---
## 11 Pruebas de Caja Negra y Caja de Cristal 🧪
### 11.1 Pruebas de Caja Negra 🖤
- Se basan en la especificación de la función o programa.
- Prueban inputs y validan outputs.
- Unit Testing: Pruebas unitarias para cada función.
- Integration Testing: Pruebas de integración entre módulos.

Ejemplo de código:

```python
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
```
### 11.2 Pruebas de Caja de Cristal 💎
- Se basan en el flujo del programa.
- Prueban todos los caminos posibles, incluyendo ramificaciones, bucles y recursión.
- Regression Testing: Pruebas de regresión para detectar problemas después de cambios.

Ejemplo de código:

```python
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
```

---
## 12 Excepciones 🚨
Las excepciones son comunes en programación y se utilizan para manejar errores.

Manejo de Excepciones

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: División por cero")
finally:
    print("Finalizado")
```

Crear Excepciones Personalizadas

```python
raise ValueError("Este es un error personalizado")
```

---
# PARTE 3 - Algoritmos de Menor a Mayor Complejidad 📊
En esta sección, se presentan los algoritmos proporcionados, ordenados de menor a mayor complejidad, con el objetivo de que el lector entienda cómo cada programa contribuye al aprendizaje de Python básico

---
### 1 break_continue.py 🔄
Este script demuestra el uso de estructuras de control en Python, como bucles `for`,`break` y `continue`.

El código imprime 'NA' 12 veces y luego 'HEY JUDE'.

```python
def run():
    for i in range(13):
        if i == 12:
            print('HEY JUDE')
            break
        print('NA')

if __name__ == '__main__':
    run()
```

---
### 2 conditionals.py 🔄
Programa que evalúa si un número ingresado por el usuario es mayor, menor o igual a 5.
Este ejemplo introduce la estructura condicional **if-elif-else** en Python.

```python
# Request a number from the user
number = int(input('Enter a number: '))

# Evaluate the entered number
if number > 5:
    print('It is greater than 5')
elif number == 5:
    print('It is equal to 5')
else:
    print('It is less than 5')
```

---
### 3 converter.py 💱
Convierte una cantidad de pesos colombianos a dólares según una tasa de cambio fija. Introduce el manejo de entrada de usuario y operaciones aritméticas.

```python
def convert_pesos_to_dollars():
    pesos_col = float(input("How many Colombian pesos do you have? "))
    dollar_value = 3875  # Fixed exchange rate
    dollars = round(pesos_col / dollar_value, 2)
    print("You have $ " + str(dollars) + " dollars")

if __name__ == '__main__':
    convert_pesos_to_dollars()
```

---
### 4 dictionaries.py 📚
Muestra cómo definir un diccionario, acceder a sus valores y recorrerlo con un bucle. Es útil para entender estructuras de datos clave-valor.

```python
def run():
    # Dictionary with the population of some countries
    country_population = {
        'Argentina': 44938712,
        'Brazil': 210147125,
        'Colombia': 50378478
    }

    # Iterate over the dictionary and print each country with its population
    for country, population in country_population.items():
        print(country + " has " + str(population) + " inhabitants.")

if __name__ == '__main__':
    run()

```
---
### 5 for.py 🔁
Ejemplo de uso de bucles for y while. Introduce la función range() y cómo generar listas con ella.

```python
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
```

---
### 6 game.py 🎮
Este programa es un simple juego de adivinanza en el que el usuario debe adivinar un número aleatorio generado por el programa.

Conceptos básicos de Python aplicados:

- Uso del módulo random para generar números aleatorios.
- Entrada de usuario con input() y conversión a entero.
- Uso de estructuras condicionales if-else.
- Bucle while para repetir la interacción hasta acertar.

```python
import random

def run():
    random_number = random.randint(1, 100)
    chosen_number = int(input('Elige un número del 1 al 100: '))
    while random_number != chosen_number:
        if chosen_number < random_number:
            print('Elige un número más grande')
        else:
            print('Elige un número más pequeño')
        chosen_number = int(input('Elige otro número: '))
    print("¡Ganaste!")
```

---
### 7 loops.py 🔄
Calcula y muestra las potencias de 2 hasta alcanzar un límite específico. Introduce el uso de bucles while y operaciones matemáticas.

```python
def main():
    limit = 1000000
    counter = 0
    power_of_2 = 2 ** counter  # 2 raised to the power of the counter

    # While loop to calculate powers of 2 until the limit is reached
    while power_of_2 < limit:
        print('2 raised to ' + str(counter) + ' is equal to: ' + str(power_of_2))
        counter = counter + 1
        power_of_2 = 2 ** counter

if __name__ == '__main__':
    main()
```

---
### 8 palindrome.py 🔄
Verifica si una palabra o frase es un palíndromo. Introduce el manejo de cadenas y operaciones de slicing.

```python
# Function that checks if a word or phrase is a palindrome
def palindrome(word):
    word = word.replace(' ', '')  # Removes spaces
    word = word.lower()  # Converts everything to lowercase
    reversed_word = word[::-1]  # Reverses the string

    return word == reversed_word  # Returns True if it is a palindrome, False if not

# Main function that asks for a word and checks if it is a palindrome
def run():
    word = input('Enter a word: ')
    if palindrome(word):
        print('It is a palindrome')
    else:
        print('It is not a palindrome')


if __name__ == '__main__':
    run()
```

---
### 9 password.py 🔒
Genera una contraseña aleatoria de 15 caracteres. Introduce el uso de listas, bucles for y la función random.choice.

```python
import random

# Function that generates a random 15-character password
def generate_password():
    # Lists of possible characters for the password
    uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    symbols = ['!', '#', '$', '&', '/', '(', ')']
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    # Combine all character lists into one
    characters = uppercase + lowercase + symbols + numbers

    # List to store the password characters
    password = []

    # Generate 15 random characters
    for i in range(15):
        random_character = random.choice(characters)  # Chooses a random character
        password.append(random_character)  # Adds the character to the list

    # Join the characters into a string and return it
    password = "".join(password)
    return password

def run():
    password = generate_password()  # Calls the function that generates the password
    print('Your new password is: ' + password)  # Displays the generated password

# Executes the 'run' function only if this file is run directly
if __name__ == '__main__':
    run()

```
---
### 10 prime_number.py 🔢
Este programa verifica si un número es primo .
Un numero es primo cuando el residuo de la divicion es 0 solo cuando se divide entre uno, y entre el mismo numero.

Conceptos básicos de Python que se aplican:

- Importación de módulos (math para operaciones matemáticas).
- Funciones y su retorno de valores.
- Uso de bucles e instrucciones de control (for, if, continue).
- Entrada de usuario con  input() y conversión de tipos.

```python
import math

def is_prime_number(number):
    square_root = int(math.sqrt(number))  # Calculates the square root and converts it to an integer
    counter = 0

    for i in range(1, square_root + 1):
        if i == 1 or i == number:  # Skips 1 and the number itself
            continue
        if number % i == 0:  # Checks if it is divisible
            counter += 1

    return counter != 1  # Returns True if it is prime, False otherwise

def run():
    number = int(input('Enter the number you want: '))  # Asks the user for a number
    if is_prime_number(number):
        print('The number is prime')
    else:
        print('The number is not prime')

if __name__ == "__main__":
    run()

```
---
### 11 recorrer_cadena.py 🔄
Este programa toma una frase ingresada por el usuario y convierte cada carácter a mayúsculas.

- Iteración sobre cadenas con un bucle for.
- Manipulación de cadenas con el método upper().

```python
def run():
    sentence = input('Enter a sentence: ')
    for character in sentence:  # Iterates over each character in the sentence
        print(character.upper())  # Converts the character to uppercase and prints it

if __name__ == "__main__":
    run()
```

### 12 aproximacion.py 📏
Este programa encuentra la raíz cuadrada de un número usando aproximaciones sucesivas.
Si el número no tiene una raíz exacta, se devuelve una aproximación con un margen de error (epsilon).

Conceptos básicos en Python:
- Entrada de datos con `input()`
- Uso de `while` para iteraciones con condición
- Operaciones con números de punto flotante
- Control de errores con margen de tolerancia (`epsilon`)

```python
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
```
---
### 13 busqueda_binaria.py 🔎
Este programa calcula la raíz cuadrada de un número utilizando el método de búsqueda binaria. Si la raíz no es exacta, devuelve una aproximación con un margen de error (`epsilon`).

Conceptos básicos en Python:
- Entrada de datos con `input()`
- Uso de `while` para iteraciones con condición
- Implementación de búsqueda binaria para encontrar valores aproximados
- Manejo de números flotantes y precisión (`epsilon`)

```python
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
```
---
### 14 enumeracion_exhaustiva.py 🔍
Este programa implementa el método de Enumeración Exhaustiva para encontrar la raíz cuadrada exacta de un número entero.

Conceptos básicos en Python:
- Uso de variables y entrada de usuario (`input`, `int`)
- Bucle `while` para iteración controlada
- Condicionales `if-else` para verificar resultados

```python
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
```
---
### 15 excepciones.py 🚨
Manejo de excepciones en Python con `try-except`.

Conceptos básicos abordados:
- Uso de listas y comprensión de listas (`list comprehension`)
- Manejo de excepciones con `try-except`
- `ZeroDivisionError` para evitar errores de división entre cero

```python
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
```
---
### 16 factorial.py 🔢
Cálculo del factorial de un número usando recursividad. Introduce el concepto de recursividad.

```python
def factorial(n):
    print(n)
    if n == 1:
        return 1
    return n * factorial(n - 1)

n = int(input("Escribe un entero positivo: "))
print(f"El factorial de {n} es {factorial(n)}")
```
---
### 17 iteraciones.py 🔄
Este programa demuestra el uso de bucles anidados en Python mediante un contador de 0 a 99.
Es ideal para aprender sobre estructuras de control, el funcionamiento de ciclos while anidados y la gestión de variables de control en iteraciones.

```python
# Counter from 0 to 99 using two nested while loops
outer_counter = 0  # Controls the tens
inner_counter = 0  # Controls the units

while outer_counter < 10:
    while inner_counter < 10:
        # Displays the current value of the counters
        print(outer_counter, inner_counter)
        inner_counter += 1  # Increments the inner counter

    outer_counter += 1  # Increments the outer counter
    inner_counter = 0   # Resets the inner counter
```
---
### 18 tres_metodos_numericos.py 📊
Implementa tres métodos para calcular la raíz cuadrada de un número: enumeración exhaustiva, aproximación y búsqueda binaria. Introduce diferentes enfoques para resolver un problema.

```python
def exhaustive_enumeration(target):
    answer = 0

    # While loop: Exhaustive enumeration
    # Increments `answer` by 1 until it finds an exact square root or surpasses the target.
    while answer**2 < target:
        answer += 1

    if answer**2 == target:
        print(f'The square root of {target} is {answer}')
    else:
        print(f'{target} does not have an exact square root')

def approximation(target):
    epsilon = 0.01  # Desired precision
    step = epsilon**2
    answer = 0.0

    # While loop: Approximation
    # Increments `answer` in small steps until the difference between `answer` squared and the target is less than `epsilon`.
    while abs(answer**2 - target) >= epsilon and answer <= target:
        answer += step
        print(f'Difference: {abs(answer**2 - target)}, Answer: {answer}')

    if abs(answer**2 - target) >= epsilon:
        print(f'Could not find the square root of {target}')
    else:
        print(f'The square root of {target} is {answer}')

def binary_search(target):
    epsilon = 0.01  # Desired precision
    low = 0.0
    high = max(1.0, target)
    answer = (high + low) / 2  # Initial midpoint

    # While loop: Binary search
    # Reduces the search range by half in each iteration until finding an approximation of the square root with the desired precision.
    while abs(answer**2 - target) >= epsilon:
        print(f'low={low}, high={high}, answer={answer}')
        if answer**2 < target:
            low = answer  # Adjusts the lower bound
        else:
            high = answer  # Adjusts the upper bound
        answer = (high + low) / 2  # Recalculates the midpoint

    print(f'The square root of {target} is {answer}')

def run():
    # Menu to select the method
    method_type = int(input('''
        1. Exhaustive Enumeration
        2. Approximation
        3. Binary Search
        Select the method: '''))

    num = int(input('Enter the number to find its square root: '))

    if method_type == 1:
        exhaustive_enumeration(num)
    elif method_type == 2:
        approximation(num)
    elif method_type == 3:
        binary_search(num)
    else:
        print('Please enter a valid option')

if __name__ == "__main__":
    run()
```

# 📝 Fuentes
- Platzi
- Python Documentation
- W3Schools-
