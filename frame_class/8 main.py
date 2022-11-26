import time


def main():
    init()

    grey = (128, 128, 128)
    orange = (255, 97, 3)
    red = (213, 50, 80)
    green = (47, 79, 79)
    white = (255, 248, 220)
    Gainsboro = (220, 220, 220)

    scrn_size = (weight, height)
    scrn = pygame.display.set_mode((svrn_size))
    pygame.display.set_caption('Snake Game')

    snake_head = Snakehead(scrn)
    snake_body = Snakebody(scrn)
    snake_body.headFollow = snake_head

    fruit_obj = Fruit(scrn)
    fruit_obj.snakes = snake_body

    clock = time.clock()
