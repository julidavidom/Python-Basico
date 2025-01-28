# 🐍 **Introducción al funcionamiento Python** 🚀

Bienvenido a la **Introducción al funcionamiento Python**, donde descubrirás las características fundamentales de Python y cómo aprovecharlas al máximo.

---https://github.com/julidavidom/Python1/tree/main

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
### 🔗 Tipos Complejos en Python
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
Aunque Python es un lenguaje de tipado dinámico, puedes usar la herramienta mypy para realizar un análisis estático de los tipos en tu código. Esto es especialmente útil para asegurarte de que los tipos son correctos antes de ejecutar el código.


## 🚀 Ventajas del Tipado Estático
**Claridad:** Mejora la legibilidad del código.
**Prevención de errores:**  Detecta problemas antes de la ejecución.
**Colaboración:** Facilita el trabajo en equipos de desarrollo grandes.
**Seguridad:** Reduce la probabilidad de errores complejos que son difíciles de detectar en proyectos grandes.

## 🌟 Conclusión
Este README proporciona una introducción al mundo de Python, desde su funcionamiento hasta el uso de tipado y la organización de proyectos. ¡Ahora estás listo para comenzar a escribir código Python eficiente y bien estructurado!
