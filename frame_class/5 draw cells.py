def rect(self, color, scrn):
    cell_width = weigth / COL
    cell_height = height / ROW
    left = self.col * cell_width
    top = self.row * cell_height
    draw.rect(scrn, color, [left, top, cell_width, cell_height])
    pass