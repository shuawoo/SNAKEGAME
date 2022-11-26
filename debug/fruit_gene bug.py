def creat(self):
    self.pos = Point(row=random.randint(1, ROW - 1), col=random.randint(1, COL - 1))
    for i in self.snakes.body:
        if i.row == self.pos.row and i.col == self.pos.col:
            self.creat()
            pass