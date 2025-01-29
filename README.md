# 🐍 **Introducción al funcionamiento Python** 🚀

Bienvenido a la **Introducción al funcionamiento Python**, donde descubrirás las características fundamentales de Python y cómo aprovecharlas al máximo.

---

# 🧑‍💻 **¿Cómo Funciona Python?**

Python es un lenguaje **interpretado**, lo que significa que el código no se traduce directamente a código de máquina como en los lenguajes compilados, sino que pasa por un proceso de interpretación que lo convierte en un formato intermedio (bytecode) que la máquina puede ejecutar.

### 📝 **Lenguajes Compilados** (Ejemplo: C++)

Los lenguajes compilados, como **C++**, convierten el código fuente a código de máquina directamente mediante un proceso de compilación. Este tipo de lenguajes suelen ser más rápidos en tiempo de ejecución.

```plaintext
C++ -----> compilador -----> código de máquina
```

### 🔄 Lenguajes Interpretados (Ejemplo: Python)
En Python, el código pasa por una máquina virtual que convierte el código a un formato intermedio (bytecode), y luego lo ejecuta. Esto hace que Python sea multiplataforma y fácil de usar en diferentes sistemas operativos.

```plaintext
Python -----> bytecode -----> máquina virtual de Python -----> ejecución
```
---
## 🧑‍🔧 Preguntas Frecuentes
### ⚡ ¿Son los lenguajes interpretados más lentos?
En general, sí, pero la versatilidad y facilidad de uso de Python lo hacen ideal para muchas aplicaciones como análisis de datos, machine learning y desarrollo web. En muchos casos, la diferencia en velocidad no es un factor limitante.

### 🧹 ¿Qué es el Garbage Collector en Python?
Python incluye un recolector de basura que se encarga de liberar memoria automáticamente eliminando objetos no utilizados. Esto mejora la eficiencia y previene problemas de memoria.

### 🗂️ ¿Qué es la carpeta _pycache_?
La carpeta **_pycache_**  contiene el bytecode de los archivos Python, lo que optimiza la ejecución del código al evitar la recompilación innecesaria en ejecuciones futuras.

--- 

## 📁 Organización de los Archivos de tu Proyecto
Es esencial tener una buena organización en los proyectos Python, especialmente cuando crecen en tamaño y complejidad. Python organiza su código en módulos y paquetes.

### 📦 Módulos
Un módulo es cualquier archivo de Python .py que contiene código reutilizable. Ejemplos comunes incluyen math, random, y os.

### 📂 Paquetes
Un paquete es una carpeta que contiene módulos y debe incluir un archivo especial llamado __init__.py. Este archivo indica que la carpeta es un paquete de Python.

### Ejemplo de estructura de proyecto:

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
## 🔤 Tipado en Python
Python es un lenguaje dinámico, pero puedes utilizar anotaciones de tipo para mejorar la claridad de tu código.


### 📝 Tipado Estático vs Dinámico
En lenguajes estáticos como C++ o Java, debes especificar el tipo de cada variable.
En Python, puedes declarar variables sin un tipo específico, y el tipo se asignará dinámicamente durante la ejecución.

### 📏 Tipado Estático en Python
Aunque Python es dinámico, desde la versión 3.5, puedes usar anotaciones de tipo para hacer el código más legible y fácil de depurar.

```python
# Anotación de tipo para variables
a: int = 5
b: str = 'Hola'
c: bool = True
```
### 🧮 Funciones con Tipado Estático
Puedes añadir anotaciones de tipo a las funciones para definir qué tipo de datos aceptan y devuelven.

```python
def suma(a: int, b: int) -> int:
    return a + b
resultado = suma(3, 4)
print(resultado)
```

### 📊 Listas y Diccionarios con Tipado Estático
El módulo typing te permite declarar los tipos de los elementos en listas y diccionarios.

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
### 🔢 Tuplas con Tipado Estático
Las tuplas son colecciones inmutables que también pueden tener tipos definidos.

```python
from typing import Tuple

# Tupla con un entero, un flotante y un entero
valores: Tuple[int, float, int] = (1, 3.14, 5)
```
### 🔗 Tipados Complejos en Python
Puedes combinar diferentes tipos utilizando el módulo typing, lo que permite crear estructuras complejas como listas de diccionarios con tuplas.

```python
from typing import Dict, List, Tuple

# Lista de diccionarios, donde cada diccionario tiene como valor una tupla de enteros
coordenadas: List[Dict[str, Tuple[int, int]]] = [
    {"coord1": (1, 2), "coord2": (3, 5)},
    {"coord1": (0, 1), "coord2": (2, 5)}
]
```
---
## 🔨 Recomendación de Herramientas
Aunque Python es un lenguaje de tipado dinámico, puedes usar la herramienta mypy para realizar un análisis estático de los tipos en tu código. Esto es especialmente útil para asegurarte de que los tipados son correctos antes de ejecutar el código.

## 🚀 Ventajas del Tipado Estático
**Claridad:** Mejora la legibilidad del código.
**Prevención de errores:**  Detecta problemas antes de la ejecución.
**Colaboración:** Facilita el trabajo en equipos de desarrollo grandes.
**Seguridad:** Reduce la probabilidad de errores complejos que son difíciles de detectar en proyectos grandes.

---
# Guía de Conceptos de Programación 📚

Este archivo proporciona un resumen completo sobre **lenguajes de programación**, **tipos de datos**, **operaciones matemáticas**, **iteraciones**, **flotantes** y más. Es útil tanto para principiantes como para programadores experimentados que desean repasar conceptos esenciales.

## 1. ¿Qué es un lenguaje de programación? 💻

Un **lenguaje de programación** es un lenguaje formal que, mediante una serie de instrucciones, permite al programador escribir un conjunto de órdenes, acciones consecutivas, datos y algoritmos para crear programas que controlen el comportamiento físico y lógico de una máquina.

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

## 3. Lenguajes interpretados y compilados 🔄

### 3.1 Lenguaje compilado ⚙️

Requiere un paso adicional de compilación antes de ser ejecutado, lo que convierte el código en lenguaje de máquina. Ejemplos: C, C++, Java, Go, Rust.

### 3.2 Lenguaje interpretado 📜

Es convertido a lenguaje de máquina a medida que se ejecuta. Ejemplos: Python, Ruby, JavaScript.

---
## 4. ¿Qué es un objeto? 🏷️

Un **objeto** es un concepto, abstracción o cosa con límites bien definidos que tiene un significado dentro del problema que se está manejando.

---

## 5. Tipos de datos básicos en programación 🧮

Los tipos de datos más comunes son:

- `int`: Números enteros.
- `float`: Números con decimales.
- `bool`: Valores booleanos (`True` o `False`).
- `str`: Cadenas de texto.

### Ejemplo de definición de variables:

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

### Puntos clave:
- Las iteraciones se pueden anidar (escribir iteraciones dentro de otras).
- break se utiliza para salir anticipadamente de una iteración.
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

**- ¿Por qué no se representan de manera exacta?`**

En las computadoras, los números flotantes no se pueden representar con total precisión. Esto ocurre porque algunos valores, como 0.1, no tienen una representación exacta en binario debido a las limitaciones de la cantidad de dígitos significativos que pueden ser almacenados.

---
## 9. Representación binaria 🔢
**- Cómo funciona:** Los números se representan como secuencias de 0s y 1s en binario.

**- El problema:** Algunos números decimales no pueden ser representados exactamente en este formato.

**Ejemplos:**
El número 0.625 tiene una representación exacta en binario: 101 * 2**-3.
Sin embargo, 0.1 no puede representarse de forma precisa. En su lugar, se aproxima a un valor cercano, lo que genera un error de representación.

---
## 10. Precisión en Python 🐍
Python utiliza 53 bits de precisión para manejar números flotantes en la mayoría de las implementaciones modernas.
Esto significa que números como 0.1 son extremadamente cercanos a su valor real, pero nunca exactamente iguales.
Ejemplo de resultado inesperado:


```python
0.1000000000000000055511151231257827021181583404541015625
```
### Buenas prácticas para trabajar con flotantes ✅

Debido a estas imprecisiones, no compares números flotantes con el operador ==. En su lugar, utiliza comparaciones aproximadas.

**Ejemplo:**

```python
abs(x - 1.0) < 1e-9  # Verifica si la diferencia es lo suficientemente pequeña

```
## 📝 Fuentes
Python Documentation - W3Schools - Platzi
