import plotly.express as px
from die import Die

# Crea un D6 y un D10.
die_1 = Die()
die_2 = Die(10)

# Hace algunas tiradas y guarda los resultados en una lista.
results = []
for roll_num in range(50_000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analiza los resultados.
frequencies = []    # Creamos una lista vacia.
max_result = die_1.num_sides + die_2.num_sides
poss_results = range(2, max_result + 1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualiza los resultados.
title = 'Results of Rolling a D6 and a D10 50,000 Times'
labels = {'x': 'Result', 'y': 'Frecuency of Result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

# Añade personalizaciones al gràfico.
fig.update_layout(xaxis_dtick=1)

fig.show()