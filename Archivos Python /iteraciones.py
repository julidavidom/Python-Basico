'''
Este programa demuestra el uso de bucles anidados en Python mediante un contador de 0 a 99.
Es ideal para aprender sobre estructuras de control, el funcionamiento de ciclos while anidados
y la gestión de variables de control en iteraciones.
'''
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
