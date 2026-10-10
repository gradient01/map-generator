import numpy as np
import random

MAP_SIZE = 200

map = np.zeros(MAP_SIZE**2, dtype=np.uint8) #"dtype=np.uint8" really important for optimization, heights are between 0 and 255

def set_map(x, y, value):
    map[y * MAP_SIZE + x] = value

def get_map(x, y):
    return map[y * MAP_SIZE + x]

def generate_map():
    """
    First version of the map generation algorithm
    """
    random.seed()

    steps = [50, 20, 8]
    weights = [0.60, 0.28, 0.12]

    grids = []

    for step in steps:
        n = (MAP_SIZE - 1) // step + 2
        grid = []

        for gy in range(n):
            row = []
            for gx in range(n):
                row.append(random.random())
            grid.append(row)

        grids.append(grid)
        
    for y in range(MAP_SIZE):
        for x in range(MAP_SIZE):
            h = 0.0

            for k in range(3):
                step = steps[k]
                grid = grids[k]

                ix = x // step
                iy = y // step

                tx = (x % step) / step
                ty = (y % step) / step

                a = grid[iy][ix] * (1 - tx) + \
                    grid[iy][ix + 1] * tx

                b = grid[iy + 1][ix] * (1 - tx) + \
                    grid[iy + 1][ix + 1] * tx

                h += weights[k] * (
                    a * (1 - ty) + b * ty
                )

            set_map(x, y, int(h * 255))


if __name__ == "__main__":
    generate_map()