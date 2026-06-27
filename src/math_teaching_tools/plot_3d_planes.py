from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np


def main() -> None:
    figure = plt.figure()
    axis = figure.add_subplot(111, projection="3d")

    x_values = np.linspace(-20, 30, 100)
    y_values = np.linspace(-20, 30, 100)
    x_grid, y_grid = np.meshgrid(x_values, y_values)

    first_plane = -x_grid + 2 * y_grid + 5
    second_plane = -x_grid + 3 * y_grid

    axis.plot_surface(x_grid, y_grid, first_plane, color="blue", alpha=0.5)
    axis.plot_surface(x_grid, y_grid, second_plane, color="red", alpha=0.5)

    y_line = 5
    x_line = np.linspace(-20, 30, 100)
    z_line = -x_line + 3 * y_line
    axis.plot(x_line, np.full_like(x_line, y_line), z_line, color="black", linewidth=2)

    axis.set_axis_off()
    plt.show()


if __name__ == "__main__":
    main()
