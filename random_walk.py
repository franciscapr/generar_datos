from random import choice

class RandomWalk:
    """Una clase para generar caminatas aleatorias."""

    def __init__(self, num_points=5000):
        """Inicializa los atributos de una caminta."""
        self.num_points = num_points

        # Todos los caminos empiezan en (0, 0).
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Calcula todos los puntos del paseo."""

        # Sigue dando pasos hasta que la caminata alcanza la longitud deseada.
        while len(self.x_values) < self.num_points:

            # Decide en què direcciòn ir y cuànto avanzar en esa direcciòn.
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            # Rechaza movimientos que no van a ninguna parte.
            if x_step == 0 and y_step == 0:
                continue

            # Calcula la nueva posiciòn.
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)