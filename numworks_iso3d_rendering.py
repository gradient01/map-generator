from kandinsky import fill_rect
from map_generator import *

SCREEN_W=320
SCREEN_H=222
SCREEN_HALF_W=SCREEN_W//2
SCREEN_HALF_H=SCREEN_H//2
COEFF = 2
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