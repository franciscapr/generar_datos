import matplotlib.pyplot as plt

x_values = range(1, 5001)
y_values = [x ** 3 for x in x_values]

plt.style.use('Solarize_Light2')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.viridis, s=8)

# Establece el tìtulo del gràfico y las etiquetas de los ejes.
ax.set_title("Cubic Numbers", fontsize=24)
ax.set_xlabel("Cube of Value", fontsize=14)
ax.set_ylabel("Cube of Value", fontsize=14)

# Establece el tamaño de las etiquetas de los puntos de los ejes.
ax.tick_params(labelsize=14)

ax.axis([0, 5001, 0, 125_000_000_000])
# ax.ticklabel_format(style='plain')

# plt.savefig('Squares_plot.png', bbox_inches='tight')
plt.show()