import pygame

green = (47, 79, 79)
grey = (128, 128, 128)

def show_speed(speed):
    from main import scrn
    score_font = pygame.font.SysFont("bahnschrift", 25)
    speed_value = score_font.render('speed:' + str(speed), True, grey)
    scrn.blit(speed_value, [8, 30])


def your_snake(snake_block, snake_list):
    '''Snake'''
    from main import scrn
    for x in snake_list:
        pygame.draw.rect(scrn, green, [x[0], x[1], snake_block, snake_block])