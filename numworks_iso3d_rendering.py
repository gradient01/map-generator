from kandinsky import fill_rect
from map_generator import *

SCREEN_W=320
SCREEN_H=222
SCREEN_HALF_W=SCREEN_W//2
SCREEN_HALF_H=SCREEN_H//2
COEFF = 2
Y_COEFF = 1
SIZE = 10
B = SIZE
A = SIZE * COEFF

def draw_lozenge(x, y, color):
    for dy in range(B):
        fill_rect(x+dy*COEFF, y-dy, COEFF, -2*(B-dy), color)
    for dy in range(B):
        fill_rect(x-COEFF-dy*COEFF, y-dy, COEFF, -2*(B-dy), color)

def draw_right_parallelogram(x, y, h, color):
    for dy in range(B):
        fill_rect(x+dy*COEFF, y-dy, COEFF, h, color)

def draw_left_parallelogram(x, y, h, color):
    for dy in range(B):
        fill_rect(x-COEFF-dy*COEFF, y-dy, COEFF, h, color)

def lcolor(px, py, h):
    return (0, 200 + 20*((px + py)%2), 0)

def rpcolor(px, py, h):
    return (100 + 20*((px + py)%2),)*3

def lpcolor(px, py, h):
    return (150 + 20*((px + py)%2),)*3

def render(dx, dy):
    """
    v2: Not enough optimization
    """
    for px in range(MAP_SIZE):
        for py in range(MAP_SIZE):
            h = map[py * MAP_SIZE + px]
            x = SCREEN_HALF_W + (px - py) * A + dx
            y = SCREEN_HALF_H + (px + py) * B - h * Y_COEFF + dy
            draw_lozenge(x, y, lcolor(px, py, h))
            dh = h - get_map(px+1, py)
            if dh > 0:
                draw_right_parallelogram(x, y, dh * Y_COEFF, rpcolor(px, py, h))
            dh = h - get_map(px, py+1)
            if dh > 0:
                draw_left_parallelogram(x, y, dh * Y_COEFF, lpcolor(px, py, h))