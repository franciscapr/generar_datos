import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.style.use('seaborn-v0_8')
# Solarize_Light2

plt.scatter(2, 4, s=200)


fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)

# Establece el tìtulo del gràfico y las etiquetas de los ejes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Square of Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Establece el tamaño de las etiquetas de los puntos de los ejes.
ax.tick_params(labelsize=14)

plt.show()
