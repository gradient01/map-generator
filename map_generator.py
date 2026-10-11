import numpy as np
import random
import math

MAP_SIZE = 200

map = np.zeros(MAP_SIZE**2, dtype=np.uint8) #"dtype=np.uint8" really important for optimization, heights are between 0 and 255

def set_map(x, y, value):
    map[y * MAP_SIZE + x] = value

def get_map(x, y):
    return map[y * MAP_SIZE + x]

def generate_map(map_size):
    """
    Second version of the map generation algorithm: Perlin noise
    """
    #random.seed(42)

    GRID_X = map_size
    GRID_Y = map_size

    CELL_SIZE = 30

    COLS = (GRID_X // CELL_SIZE) + 2
    ROWS = (GRID_Y // CELL_SIZE) + 2

    gradients = []
    for r in range(ROWS):
        row_grads = []
        for c in range(COLS):
            angle = random.uniform(0, 2 * math.pi)
            row_grads.append((math.cos(angle), math.sin(angle)))
        gradients.append(row_grads)

    def fade(t):
        return t * t * t * (t * (t * 6 - 15) + 10)

    def lerp(a, b, t):
        return a + t * (b - a)

    def dot_product(gx, gy, dx, dy):
        return gx * dx + gy * dy

    for y in range(GRID_Y):
        cell_y = y // CELL_SIZE
        yf = (y % CELL_SIZE) / CELL_SIZE
        v = fade(yf)
        
        for x in range(GRID_X):
            cell_x = x // CELL_SIZE
            xf = (x % CELL_SIZE) / CELL_SIZE
            u = fade(xf)
            
            g00 = gradients[cell_y][cell_x]
            g10 = gradients[cell_y][cell_x + 1]
            g01 = gradients[cell_y + 1][cell_x]
            g11 = gradients[cell_y + 1][cell_x + 1]
            
            n00 = dot_product(g00[0], g00[1], xf, yf)
            n10 = dot_product(g10[0], g10[1], xf - 1, yf)
            n01 = dot_product(g01[0], g01[1], xf, yf - 1)
            n11 = dot_product(g11[0], g11[1], xf - 1, yf - 1)
            nx0 = lerp(n00, n10, u)
            nx1 = lerp(n01, n11, u)
            n_final = lerp(nx0, nx1, v)
            
            val = int((n_final + 0.7) * 182) 
            val = max(0, min(255, val))

            set_map(x, y, max(0, min(255, val)))


if __name__ == "__main__":
    generate_map(MAP_SIZE)