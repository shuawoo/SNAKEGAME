import random

class SnakeHead:
    row = random.randint(1, scrn_ROW/2)
    col = random.randint(1, scrn_COL/2)
    head = Point(row=row, col=col)

    def __init__(self, scrn):
        self.scrn = scrn
        pass

    def head_move(self):
        if self.direct == 'left':
            self.head.col -= 1
        elif self.direct == 'right':
            self.head.col += 1
        elif self.direct == 'up':
            self.head.row -= 1
        elif self.direct == 'down':
            self.head.row += 1
        pass
