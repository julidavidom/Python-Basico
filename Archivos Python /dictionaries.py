"""
Ejemplo de uso de diccionarios en Python.
Se muestra cómo definir un diccionario, acceder a sus valores y recorrerlo con un bucle.
"""

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
