# framework
import random
from pygame import *

# scrn setting
scrn_weight = 800
scrn_height = 600
COL = 80
ROW = 60

# point class
class Point:
    row = 0
    col = 0

    def __init__(self, row, col):
        self.row = rpw
        self.col = col

    def copy(self):
        return Point(row=self.row, col=self.col)
