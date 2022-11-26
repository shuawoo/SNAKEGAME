class Fruit:
    row = random.randint(1, ROW-1)
    col = random.randint(1, COL-1)
    pos = Point(row=row, col=col)
    snakes = Snakebody

    def __init__(self, scrn):
        self.scrn = scrn

    def new_fruit(self):
        self.pos = Point(row = random.randint(1, ROW-1), col = random.randint(1, COL-1))
        for i in self.snakes.body:
            if i.row == self.pos.row and i.col == self.pos.col:
                self.new_fruit()
                pass
