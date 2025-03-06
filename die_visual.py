from die import Die

# Crea un D6.
die = Die()    # Creamos una instancia de Die de seis lados por defecto.

# Hace algunas tiradas y guarda los resultados en un lista.
results = []    # Creamos una lista vacia.

for roll_num in range(100):    # Tiramos el dado 100 veces
    result = die.roll()
    results.append(result)    # Almacenamos los resultados en la lista results

# Imprimimos la lista
print(results)