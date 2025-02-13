import matplotlib.pyplot as plt
import random
from random_walk import RandomWalk

class ModofiedRandomWlak(RandomWalk):
    def __init__(self, num_points=5000):
        super().__init__(num_points)

    def get_step(self):
        direction = random.choice([1, -1])
        distance = random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8])    # Lista extendida
        return direction * distance
    
    def fill_walk(self):
        while len(self.x_values) < self.num_points:
            x_step = self.get_step()
            y_step = self.get_step()

            if x_step == 0 and y_step == 0:
                continue

            self.x_values.append(self.x_values[-1] + x_step)
            self.y_values.append(self.y_values[-1] + y_step)

# Sigue generando caminatas nuevas mientras el programa estè activo.
while True:
    # Crea una caminata aleatoria con 5000 puntos.
    rw = ModofiedRandomWlak()
    rw.fill_walk()

    # Traza los puntos de la caminata con lìneas en lugar de puntos.
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(15, 9), dpi=128)
    ax.plot(rw.x_values, rw.y_values, linewidth=1)
    ax.set_aspect('equal')

    # Enfatiza el primer punto y el ùltimo.
    ax.plot(0, 0, 'go', markersize=10)
    ax.plot(rw.x_values[-1], rw.y_values[-1], 'ro', markersize=10)

    plt.show()

    keep_running = input('Make another walk? (y/n): ')
    if keep_running == 'n':
        break