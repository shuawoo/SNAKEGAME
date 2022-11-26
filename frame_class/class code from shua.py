# 1 framework
import random
import pygame
import pygame_menu

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
        self.row = row
        self.col = col

    def copy(self):
        return Point(row=self.row, col=self.col)

# 2 class snakehead
class SnakeHead:
    row = random.randint(1, ROW/2 - 1)
    col = random.randint(1, COL/2 - 1)
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

# 3 class snakebody
class SnakeBody:
    headFollow = SnakeHead
    body = Point(row=headFollow.head.row, col=headFollow.head.col + 1)

    def __init__(self, scrn):
        self.scrn = scrn

    def body_move_f(self): #move forward
        self.body.insert(0, self.headFollow.head.copy())

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


# 4 class fruit
class Fruit:
    row = random.randint(1, ROW-1)
    col = random.randint(1, COL-1)
    pos = Point(row=row, col=col)
    snakes = SnakeBody

    def __init__(self, scrn):
        self.scrn = scrn

    def new_fruit(self):
        self.pos = Point(row = random.randint(1, ROW-1), col = random.randint(1, COL-1))
        for i in self.snakes.body:
            if i.row == self.pos.row and i.col == self.pos.col:
                self.new_fruit()
                pass
            pass


# 5 draw cells
def rect(self, color, scrn):
    cell_width = scrn_weight / COL
    cell_height = scrn_height / ROW
    left = self.col * cell_width
    top = self.row * cell_height
    pygame.draw.rect(scrn, color, [left, top, cell_width, cell_height])
    pass

# 6 key control
def key_control(snake_obj):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
            pass
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if snake_obj.direct == 'left' or snake_obj.direct == 'right':
                    snake_obj.direct == 'up'
            elif event.key == pygame.K_DOWN:
                if snake_obj.direct == 'left' or snake_obj.direct == 'right':
                    snake_obj.direct == 'down'
            elif event.key == pygame.K_LEFT:
                if snake_obj.direct == 'up' or snake_obj.direct == 'down':
                    snake_obj.direct == 'left'
            elif event.key == pygame.K_RIGHT:
                if snake_obj.direct == 'up' or snake_obj.direct == 'down':
                    snake_obj.direct == 'right'
            pass


# 7 fail
def failure_check(snake_h, snake_b):
    fail = False
    # hit the bound
    if snake_h.head.col < 0 or snake_h.head.row < 0 or snake_h.head.col >= COL or snake_h.head.row >= ROW:
        fail = True
        pass
    # hit itself
    for i in snake_b.body:
        if snake_h.head.col == i.col and snake_h.head.row == i.row:
            fail = True
            break
        pass
    return fail


# 8 main
def main():
    pygame.init()

    scrn_size = (scrn_weight, scrn_height)
    scrn = pygame.display.set_mode((scrn_size))
    pygame.display.set_caption('Snake Game')

    grey = (128, 128, 128)
    orange = (255, 97, 3)
    red = (213, 50, 80)
    green = (47, 79, 79)
    white = (255, 248, 220)
    Gainsboro = (220, 220, 220)
    black = (0, 0, 0)

    snake_head = SnakeHead(scrn)
    snake_body = SnakeBody(scrn)
    snake_body.headFollow = snake_head

    fruit_obj = Fruit(scrn)
    fruit_obj.snakes = snake_body

    clock = pygame.time.Clock()


# 9 loop
    while True:
        key_control(snake_head)

        if snake_head.head.row == fruit_obj.pos.row and snake_head.head.col == fruit_obj.pos.col:
            fruit_obj.new_fruit()
            snake_body.body_add()
            pass

        snake_body.body_move()
        snake_head.head_move()

        if failure_check(snake_head, snake_body):
            exit()
            pass

        pygame.draw.rect(scrn, white, (0, 0, scrn_weight, scrn_height))
        pygame.draw.rect(snake_head.head, green, scrn)
        for i in snake_body.body:
            pygame.draw.rect(i, black, scrn)
            pass
        pygame.draw.rect(fruit_obj.pos, orange, scrn)

        pygame.display.update()

        clock.tick(10)
        pass

    pass

if __name__ == '__main__':
    main()