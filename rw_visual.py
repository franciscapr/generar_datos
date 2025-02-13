import matplotlib.pyplot as plt
from random_walk import RandomWalk

# Sigue generando caminatas nuevas mientras el programa estè activo.
while True:
    # Crea una caminata aleatoria.
    rw = RandomWalk()
    rw.fill_walk()

    # Traza los puntos de la caminata.
    plt.style.use('classic')
    fig, ax = plt.subplots()
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=15)

    ax.set_aspect('equal')
    plt.show()

    keep_running = input('Make another walk? (y/n): ')
    if keep_running == 'n':
        break