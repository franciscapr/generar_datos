import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x ** 2 for x in x_values]

plt.style.use('Solarize_Light2')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=10, color='pink')

# Establece el tìtulo del gràfico y las etiquetas de los ejes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Square of Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Establece el tamaño de las etiquetas de los puntos de los ejes.
ax.tick_params(labelsize=14)

ax.axis([0, 1100, 0, 1_100_000])
ax.ticklabel_format(style='plain')

plt.show()