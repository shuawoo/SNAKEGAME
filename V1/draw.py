import pygame

class Point:
    row = 0
    col = 0
    def __init__(self, row, col):
        self.row = row
        self.col = col
    def copy(self):
        return Point(row=self.row, col=self.col)


def rect(point, color):
    from main import cell, scrn
    left = point.col * cell
    top = point.row * cell
    pygame.draw.rect(scrn, color, (left, top, cell, cell))