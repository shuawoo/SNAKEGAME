class SnakeBody:
    headFollow = Snakehead
    body = Point(row=headFollow.head.row, col=headFollow.head.col + 1)

    def __init__(self, scrn):
        self.scrn = scrn

    def body_move_f(self): #move forward
        self.body,insert(0, self.headFollow.head.copy())

    def body_move_b(self): #delete backone
        self.body.pop()

    def body_move(self):
        self.body_move_f()
        self.body_move_b()

    def body_add(self):
        self.body_move_f()
        if self.headFollow.direct == 'left':
            self.headFollow.head.col -= 1
        elif self.headFollow.direct == 'right':
            self.headFollow.head.col += 1
        elif self.headFollow.direct == 'up':
            self.headFollow.head.row -= 1
        elif self.headFollow.direct == 'down':
            self.headFollow.head.row += 1


