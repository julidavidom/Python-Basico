"""
Ejemplo de uso de diccionarios en Python.
Se muestra cómo definir un diccionario, acceder a sus valores y recorrerlo con un bucle.
"""

def run():
    # Diccionario con la población de algunos países
    poblacion_paises = {
        'Argentina': 44938712,
        'Brasil': 210147125,
        'Colombia': 50378478
    }

    # Recorremos el diccionario e imprimimos cada país con su población
    for pais, poblacion in poblacion_paises.items():
        print(pais + " tiene " + str(poblacion) + " habitantes.")

if __name__ == '__main__':
    run()
