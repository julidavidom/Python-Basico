"""
Convierte una cantidad de pesos colombianos a dólares según una tasa de cambio fija.
El usuario ingresa el monto en COP y recibe el equivalente en USD redondeado a dos decimales.
"""
def convert_pesos_to_dollars():
    pesos_col = float(input("How many Colombian pesos do you have? "))
    dollar_value = 3875  # Fixed exchange rate
    dollars = round(pesos_col / dollar_value, 2)
    print("You have $ " + str(dollars) + " dollars")

if __name__ == '__main__':
    convert_pesos_to_dollars()
