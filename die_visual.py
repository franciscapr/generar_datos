from die import Die
import plotly.express as px

# Crea un D6.
die = Die()    # Creamos una instancia de Die de seis lados por defecto.

# Hace algunas tiradas y guarda los resultados en un lista.
results = []    # Creamos una lista vacia.

for roll_num in range(1000):    # Tiramos el dado 100 veces
    result = die.roll()
    results.append(result)    # Almacenamos los resultados en la lista results

# Imprimimos la lista
# print(results)

# Analiza los resultados.
frequencies = []    # Creamos una lista vacia.
poss_results = range(1, die.num_sides+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)
print(frequencies)


# Visualiza los resultados.
title = "Results of Rolling One D6 1,000 Times"
labels = {'x': 'Result', 'y': 'Frecuency of Result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
fig.show()