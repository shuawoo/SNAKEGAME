import pygame

scrn_width = 800
scrn_height = 600
COL = 80
cell = scrn_width / COL
scrn = pygame.display.set_mode((scrn_width, scrn_height))

class Point:
    row = 0
    col = 0
    def __init__(self, row, col):
        self.row = row
        self.col = col
    def copy(self):
        return Point(row=self.row, col=self.col)


def rect(point, color):
    left = point.col * cell
    top = point.row * cell
    pygame.draw.rect(scrn, color, (left, top, cell, cell))