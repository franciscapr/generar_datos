from die import Die
import plotly.express as px

# Crea dos dados D6.
die_1 = Die()
die_2 = Die()    # Creamos una instancia de Die de seis lados por defecto.

# Hace algunas tiradas y guarda los resultados en un lista.
results = []    # Creamos una lista vacia.

for roll_num in range(1000):    # Tiramos el dado 100 veces
    result = die_1.roll() + die_2.roll()
    results.append(result)    # Almacenamos los resultados en la lista results

# Imprimimos la lista
# print(results)

# Analiza los resultados.
frequencies = []    # Creamos una lista vacia.
max_result = die_1.num_sides + die_2.num_sides
poss_results = range(2, max_result + 1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualiza los resultados.
title = "Results of Rolling Two D6 Dice 1,000 Times"
labels = {'x': 'Result', 'y': 'Frecuency of Result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

# Añade personalizaciones al gràfico.
fig.update_layout(xaxis_dtick=1)

fig.show()