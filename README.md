# 🐍 PARTE 1 - Introducción al funcionamiento Python 🚀
Bienvenido a este repositorio, donde encontrarás una guía detallada y comentada sobre los fundamentos de Python. Aquí aprenderás cómo funciona internamente este lenguaje interpretado, sus características clave y la diferencia entre lenguajes compilados e interpretados. Además, se incluyen códigos prácticos y explicaciones claras para que puedas comprender mejor cada concepto.

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
## 📁 4 Organización de los Archivos de tu Proyecto
Es esencial tener una buena organización en los proyectos Python, especialmente cuando crecen en tamaño y complejidad. Python organiza su código en módulos y paquetes.

### 📦 4.1 Módulos
Un módulo es cualquier archivo de Python .py que contiene código reutilizable. Ejemplos comunes incluyen math, random, y os.

### 📂 4.2 Paquetes
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

## 🔤 5 Tipado en Python
Python es un lenguaje dinámico, pero puedes utilizar anotaciones de tipado para mejorar la claridad de tu código.

### 📝 5.1 Tipado Estático vs Dinámico
En lenguajes estáticos como C++ o Java, debes especificar el tipo de cada variable.
En Python, puedes declarar variables sin un tipo específico, y el tipo se asignará dinámicamente durante la ejecución.

### 📏 5.2 Tipado Estático en Python
Aunque Python es dinámico, desde la versión 3.5, puedes usar anotaciones de tipado para hacer el código más legible y fácil de depurar.

```python
# Anotación de tipado para variables
a: int = 5
b: str = 'Hola'
c: bool = True
```
### 🧮 5.3 Funciones con Tipado Estático
Puedes añadir anotaciones de tipado a las funciones para definir qué tipo de datos aceptan y devuelven.

```python
def suma(a: int, b: int) -> int:
    return a + b
resultado = suma(3, 4)
print(resultado)
```
### 📊 5.4 Listas y Diccionarios con Tipado Estático
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
### 🔢 5.5 Tuplas con Tipado Estático
Las tuplas son colecciones inmutables que también pueden tener tipados definidos.

```python
from typing import Tuple

# Tupla con un entero, un flotante y un entero
valores: Tuple[int, float, int] = (1, 3.14, 5)
```

### 🔗 5.6 Tipados Complejos en Python
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
## 🔨 6 Recomendación de Herramientas
Aunque Python es un lenguaje de tipado dinámico, puedes usar la herramienta mypy para realizar un análisis estático de los tipados en tu código. Esto es especialmente útil para asegurarte de que los tipados son correctos antes de ejecutar el código.

---
## 🚀 7 Ventajas del Tipado Estático
Claridad: Mejora la legibilidad del código.

- Prevención de errores: Detecta problemas antes de la ejecución.
- Colaboración: Facilita el trabajo en equipos de desarrollo grandes.
- Seguridad: Reduce la probabilidad de errores complejos que son difíciles de detectar en proyectos grandes.

---
# PARTE 2 - Guía de Conceptos de Programación 📚
En esta sección, encontrarás un recorrido completo por los conceptos esenciales de la programación en Python. Desde los tipos de datos y operaciones matemáticas hasta estructuras de control e iteraciones, este material está diseñado tanto para principiantes como para programadores que deseen reforzar sus conocimientos. Todos los códigos están comentados para facilitar su comprensión y aplicación en proyectos reales.

---
## 1. ¿Qué es un lenguaje de programación? 💻
Un lenguaje de programación es un lenguaje formal que, mediante una serie de instrucciones, permite al programador escribir un conjunto de órdenes, acciones consecutivas, datos y algoritmos para crear programas que controlen el comportamiento físico y lógico de una máquina.

---
## 2. Tipos de lenguajes de programación 🧠
Existen varios tipos de lenguajes de programación, que se clasifican principalmente en:

### 2.1 Lenguaje de bajo nivel 🔧
Son lenguajes totalmente orientados a la máquina. Sirven de interfaz y crean un vínculo inseparable entre el hardware y el software.

### 2.2 Lenguaje de alto nivel 🏅
Están diseñados para facilitar el trabajo del programador, utilizando instrucciones más fáciles de entender. Ejemplos comunes: Python, Java, JavaScript.

### 2.3 Lenguaje específico de dominio (DSL) 🎯
Son lenguajes dedicados a resolver un problema en particular y proporcionan técnicas para solucionar situaciones específicas. Estos lenguajes están ganando popularidad debido al aumento del modelaje específico de dominio.

### 2.4 Lenguaje de propósito general 🌐
Este tipo de lenguaje está diseñado para resolver todo tipo de problemas y es el más común en la programación moderna. Ejemplos incluyen Python, C++, Java, entre otros.

---
## 3. Lenguajes interpretados y compilados 🔄
### 3.1 Lenguaje compilado ⚙️
Requiere un paso adicional de compilación antes de ser ejecutado, lo que convierte el código en lenguaje de máquina. Ejemplos: C, C++, Java, Go, Rust.

### 3.2 Lenguaje interpretado 📜
Es convertido a lenguaje de máquina a medida que se ejecuta. Ejemplos: Python, Ruby, JavaScript.

---
## 4. ¿Qué es un objeto? 🏷️
Un objeto es un concepto, abstracción o cosa con límites bien definidos que tiene un significado dentro del problema que se está manejando.

---
## 5. Tipos de datos básicos en programación 🧮
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
## 6. Operaciones básicas en Python ➗
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
## 7. Iteraciones en Python 🔁
Las iteraciones nos permiten repetir un proceso varias veces. Son fundamentales en la programación para realizar tareas repetitivas.

### 7.1 Puntos clave:
- Las iteraciones se pueden anidar (escribir iteraciones dentro de otras).
- **break** se utiliza para salir anticipadamente de una iteración.
- Hay que tener cuidado con iteraciones infinitas.

---
## 8. Representación de números flotantes en Python 🏞️
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

### 8.1 Representación binaria 🔢
- Cómo funciona: Los números se representan como secuencias de 0s y 1s en binario.
- El problema: Algunos números decimales no pueden ser representados exactamente en este formato.

**Ejemplos:**
- El número 0.625 tiene una representación exacta en binario: 101 * 2**-3.
- Sin embargo, 0.1 no puede representarse de forma precisa. En su lugar, se aproxima a un valor cercano, lo que genera un error de representación.

---
### 8.2 Precisión en Python 🐍
Python utiliza 53 bits de precisión para manejar números flotantes en la mayoría de las implementaciones modernas.
Esto significa que números como 0.1 son extremadamente cercanos a su valor real, pero nunca exactamente iguales.
Ejemplo de resultado inesperado:

```python
0.1000000000000000055511151231257827021181583404541015625
```

### 8.3 Buenas prácticas para trabajar con flotantes ✅
Debido a estas imprecisiones, no compares números flotantes con el operador ==. En su lugar, utiliza comparaciones aproximadas.

**Ejemplo:**

```python
abs(x - 1.0) < 1e-9  # Verifica si la diferencia es lo suficientemente pequeña
```
---
## 🔍9 Algoritmos de Búsqueda
### 9.1 Enumeración Exhaustiva 🕵️‍♂️
- También conocido como "adivina y verifica", este método enumera todas las posibilidades.
- Es uno de los primeros algoritmos que debes probar.

Ejemplo de código:

```python
def exhaustive_enumeration(target):
    response = 0
    while response**2 < target:
        response += 1
    if response**2 == target:
        print(f"La raíz cuadrada de {target} es {response}")
    else:
        print(f"{target} no tiene una raíz cuadrada exacta")
```

### 9.2 Aproximación de Soluciones 📏
- Similar a la enumeración exhaustiva, pero no requiere una respuesta exacta.
- Podemos aproximar soluciones con un margen de error llamado epsilon.
- Epsilon es la diferencia entre la realidad y la solución. Cuanto más pequeño sea epsilon, más nos acercaremos a la solución, pero se requerirá más procesamiento.

Ejemplo de código:

```python
def approximation(target, epsilon=0.01):
    step = epsilon**2
    response = 0.0
    while abs(response**2 - target) >= epsilon and response <= target:
        response += step
    if abs(response**2 - target) >= epsilon:
        print(f"No se encontró la raíz cuadrada de {target}")
    else:
        print(f"La raíz cuadrada de {target} es aproximadamente {response}")
```

### 9.3 Búsqueda Binaria 🔎
- Requiere que el conjunto de números esté ordenado (ej. [1, 2, 3, 4, ...]).
- Es altamente eficiente, ya que reduce el espacio de búsqueda a la mitad en cada iteración.

Ejemplo de código:

```python
def binary_search(target, epsilon=0.01):
    low = 0.0
    high = max(1.0, target)
    response = (high + low) / 2
    while abs(response**2 - target) >= epsilon:
        if response**2 < target:
            low = response
        else:
            high = response
        response = (high + low) / 2
    print(f"La raíz cuadrada de {target} es aproximadamente {response}")
```

---
## 🛠 10 Funciones
### 10.1 Abstracción 🧠
No necesitas saber cómo se implementa algo, solo cómo manejarlo.

### 10.2 Descomposición 🧩
Permite dividir el código en componentes que colaboran entre sí. Piensa en mini programas que juntos forman un programa mayor.

### 10.3 Recursividad 🔄
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

### 10.4 Funciones como Objetos 🎯
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
## 11 Tuplas 📦
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
### 12 Rangos 🔢
Los rangos representan una secuencia de enteros. Son inmutables y muy eficientes en términos de memoria.

Ejemplo:

```python
my_range = range(0, 7, 2)
for i in my_range:
    print(i)  # 0, 2, 4, 6
```

---
## 13 Listas y Mutabilidad 📝
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
## 14 Diccionarios 📚
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
## 15 Pruebas de Caja Negra y Caja de Cristal 🧪
### 15.1 Pruebas de Caja Negra 🖤
- Se basan en la especificación de la función o programa.
- Prueban inputs y validan outputs.
- Unit Testing: Pruebas unitarias para cada función.
- Integration Testing: Pruebas de integración entre módulos.

Ejemplo de código:

```python
import unittest

def add(num_1, num_2):
    return num_1 + num_2

class BlackBoxTest(unittest.TestCase):
    def test_add_two_positives(self):
        result = add(10, 5)
        self.assertEqual(result, 15)

    def test_add_two_negatives(self):
        result = add(-10, -7)
        self.assertEqual(result, -17)

if __name__ == "__main__":
    unittest.main()
```
### 15.2 Pruebas de Caja de Cristal 💎
- Se basan en el flujo del programa.
- Prueban todos los caminos posibles, incluyendo ramificaciones, bucles y recursión.
- Regression Testing: Pruebas de regresión para detectar problemas después de cambios.

Ejemplo de código:

```python
import unittest

def is_adult(age):
    return age >= 18

class GlassBoxTest(unittest.TestCase):
    def test_is_adult(self):
        age = 20
        result = is_adult(age)
        self.assertEqual(result, True)

    def test_is_minor(self):
        age = 15
        result = is_adult(age)
        self.assertEqual(result, False)

if __name__ == "__main__":
    unittest.main()
```

---
## 16 Excepciones 🚨
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
## 1. break_continue.py 🔄
Este script demuestra el uso de estructuras de control en Python, como bucles for, break y continue. Es ideal para entender cómo controlar el flujo de un bucle.

```python
def run():
    for i in range(13):
        if i == 12:
            print('HEY JUDE')
            break
        print('NA')
```

---
## 2. conditionals.py 🔄
Este programa evalúa si un número ingresado por el usuario es mayor, menor o igual a 5. Introduce la estructura condicional if-elif-else.

```python
number = int(input('Escribe un número: '))
if number > 5:
    print('Es mayor a 5')
elif number == 5:
    print('Es igual a 5')
else:
    print('Es menor a 5')
```

---
## 3. converter.py 💱
Convierte una cantidad de pesos colombianos a dólares según una tasa de cambio fija. Introduce el manejo de entrada de usuario y operaciones aritméticas.

```python
def convert_pesos_to_dollars():
    pesos_col = float(input("¿Cuántos pesos colombianos tienes? "))
    dollar_value = 3875
    dollars = round(pesos_col / dollar_value, 2)
    print("Tienes $ " + str(dollars) + " dólares")
```

---
## 4. dictionaries.py 📚
Muestra cómo definir un diccionario, acceder a sus valores y recorrerlo con un bucle. Es útil para entender estructuras de datos clave-valor.

```python
def run():
    population_countries = {
        'Argentina': 44938712,
        'Brasil': 210147125,
        'Colombia': 50378478
    }
    for country, population in population_countries.items():
        print(country + " tiene " + str(population) + " habitantes.")
```
---
## 5. for.py 🔁
Ejemplo de uso de bucles for y while. Introduce la función range() y cómo generar listas con ella.

```python
counter = 1
while counter < 1000:
    print(counter)
    counter += 1

for counter in range(1000):
    print(counter)
```

---
## 6. game.py 🎮
Un juego simple que genera un número aleatorio y pide al usuario que lo adivine. Introduce el módulo random y el uso de bucles while.

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
## 7. loops.py 🔄
Calcula y muestra las potencias de 2 hasta alcanzar un límite específico. Introduce el uso de bucles while y operaciones matemáticas.

```python
def main():
    limit = 1000000
    counter = 0
    power_of_2 = 2 ** counter
    while power_of_2 < limit:
        print('2 elevado a ' + str(counter) + ' es igual a: ' + str(power_of_2))
        counter += 1
        power_of_2 = 2 ** counter
```

---
## 8. palindrome.py 🔄
Verifica si una palabra o frase es un palíndromo. Introduce el manejo de cadenas y operaciones de slicing.

```python
def is_palindrome(word):
    word = word.replace(' ', '').lower()
    reversed_word = word[::-1]
    return word == reversed_word

def run():
    word = input('Escribe una palabra: ')
    if is_palindrome(word):
        print('Es palíndromo')
    else:
        print('No es palíndromo')
```

---
## 9. password.py 🔒
Genera una contraseña aleatoria de 15 caracteres. Introduce el uso de listas, bucles for y la función random.choice.

```python
import random

def generate_password():
    uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    symbols = ['!', '#', '$', '&', '/', '(', ')']
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    characters = uppercase + lowercase + symbols + numbers
    password = []
    for i in range(15):
        random_char = random.choice(characters)
        password.append(random_char)
    return "".join(password)

def run():
    password = generate_password()
    print('Tu nueva contraseña es: ' + password)
```
---
## 10. prime_number.py 🔢
Verifica si un número es primo. Introduce el uso de módulos como math y bucles for.

---
```python
import math

def is_prime(number):
    sqrt_number = int(math.sqrt(number))
    counter = 0
    for i in range(1, sqrt_number + 1):
        if i == 1 or i == number:
            continue
        if number % i == 0:
            counter += 1
    return counter != 1

def run():
    number = int(input('Escribe el número que deseas: '))
    if is_prime(number):
        print('El número es primo')
    else:
        print('El número no es primo')
```
---
## 11. recorrer_cadena.py 🔄
Toma una frase ingresada por el usuario y convierte cada carácter a mayúsculas. Introduce el manejo de cadenas y bucles for.

```python
def run():
    phrase = input('Escribe una frase: ')
    for char in phrase:
        print(char.upper())
```

## 12. aproximacion.py 📏
Encuentra la raíz cuadrada de un número usando aproximaciones sucesivas. Introduce el manejo de números flotantes y bucles while.

```python
def find_square_root(target, epsilon=0.01):
    step = epsilon**2
    response = 0.0
    while abs(response**2 - target) >= epsilon and response <= target:
        response += step
    if abs(response**2 - target) >= epsilon:
        print(f"No se encontró la raíz cuadrada de {target}")
    else:
        print(f"La raíz cuadrada de {target} es aproximadamente {response}")
```
---
## 13. busqueda_binaria.py 🔎
Calcula la raíz cuadrada de un número utilizando el método de búsqueda binaria. Introduce el concepto de búsqueda binaria y su eficiencia.

```python
def find_square_root_binary(target, epsilon=0.01):
    low = 0.0
    high = max(1.0, target)
    response = (high + low) / 2
    while abs(response**2 - target) >= epsilon:
        if response**2 < target:
            low = response
        else:
            high = response
        response = (high + low) / 2
    print(f'La raíz cuadrada de {target} es aproximadamente {response}')
```
---
## 14. caja_de_cristal.py 🧪
Evalúa si una persona es mayor de edad utilizando una función y pruebas unitarias con unittest. Introduce el uso de pruebas unitarias.

```python
import unittest

def is_adult(age):
    return age >= 18

class GlassBoxTest(unittest.TestCase):
    def test_is_adult(self):
        age = 20
        result = is_adult(age)
        self.assertEqual(result, True)

    def test_is_minor(self):
        age = 15
        result = is_adult(age)
        self.assertEqual(result, False)

if __name__ == "__main__":
    unittest.main()
```
---
## 15. caja_negra.py 🖤
Implementa una función para sumar dos números y la valida mediante pruebas unitarias con unittest. Introduce el uso de pruebas unitarias para funciones simples.

```python
import unittest

def add(num_1, num_2):
    return num_1 + num_2

class BlackBoxTest(unittest.TestCase):
    def test_add_two_positives(self):
        result = add(10, 5)
        self.assertEqual(result, 15)

    def test_add_two_negatives(self):
        result = add(-10, -7)
        self.assertEqual(result, -17)

if __name__ == "__main__":
    unittest.main()
```

## 16. enumeracion_exhaustiva.py 🔍
Implementa el método de Enumeración Exhaustiva para encontrar la raíz cuadrada exacta de un número entero. Introduce el concepto de enumeración exhaustiva.

```python
target = int(input("Escoge un entero: "))
response = 0
while response**2 < target:
    response += 1
if response**2 == target:
    print(f"La raíz cuadrada de {target} es {response}")
else:
    print(f"{target} no tiene una raíz cuadrada exacta")
```
---
## 17. excepciones.py 🚨
Manejo de excepciones en Python con try-except. Introduce el manejo de errores en Python.

```python
def divide_list_elements(list, divisor):
    try:
        return [i / divisor for i in list]
    except ZeroDivisionError as error:
        print(f"Error: {error}")
        return list

list = list(range(10))
divisor = 0
print(divide_list_elements(list, divisor))
```
---
## 18. factorial.py 🔢
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
## 19. iteraciones.py 🔄
Ejemplo de iteraciones anidadas con while. Introduce el concepto de bucles anidados.

```python
external_counter = 0
internal_counter = 0
while external_counter < 10:
    while internal_counter < 10:
        print(external_counter, internal_counter)
        internal_counter += 1
    external_counter += 1
    internal_counter = 0
```
---
## 20. tres_metodos_numericos.py 📊
Implementa tres métodos para calcular la raíz cuadrada de un número: enumeración exhaustiva, aproximación y búsqueda binaria. Introduce diferentes enfoques para resolver un problema.

```python
def exhaustive_enumeration(target):
    response = 0
    while response**2 < target:
        response += 1
    if response**2 == target:
        print(f'La raíz cuadrada de {target} es {response}')
    else:
        print(f'{target} no tiene una raíz cuadrada exacta')

def approximation(target, epsilon=0.01):
    step = epsilon**2
    response = 0.0
    while abs(response**2 - target) >= epsilon and response <= target:
        response += step
    if abs(response**2 - target) >= epsilon:
        print(f'No se encontró la raíz cuadrada de {target}')
    else:
        print(f'La raíz cuadrada de {target} es {response}')

def binary_search(target, epsilon=0.01):
    low = 0.0
    high = max(1.0, target)
    response = (high + low) / 2
    while abs(response**2 - target) >= epsilon:
        if response**2 < target:
            low = response
        else:
            high = response
        response = (high + low) / 2
    print(f'La raíz cuadrada de {target} es {response}')

def run():
    method = int(input('''
        1. Enumeración exhaustiva
        2. Aproximación
        3. Búsqueda binaria
        Seleccione el método: '''))
    print("Finalizado")

    num = int(input('Ingrese el número que deseas conocer la raiz cuadrada: '))

    if tipo_metodo == 1:
        enum_exhaustivo(num)
    elif tipo_metodo == 2:
        aproximacion(num)
    elif tipo_metodo == 3:
        busqueda_binaria(num)
    else:
        print('Ingrese una opción válida')

if __name__ == "__main__":
    run()
```

## 📝 Fuentes
- Python
- Python Documentation
- W3Schools-
