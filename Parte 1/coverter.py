"""
Convierte una cantidad de pesos colombianos a dólares según una tasa de cambio fija.
El usuario ingresa el monto en COP y recibe el equivalente en USD redondeado a dos decimales.
"""

def convertir_pesos_a_dolares():
    pesos_col = float(input("¿Cuántos pesos colombianos tienes? "))
    valor_dolar = 3875  # Tasa de cambio fija
    dolares = round(pesos_col / valor_dolar, 2)
    print("Tienes $ " + str(dolares) + " dólares")


if __name__ == '__main__':
    convertir_pesos_a_dolares()