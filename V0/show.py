import pygame

scrn_width = 800
scrn_height = 600
scrn = pygame.display.set_mode((scrn_width, scrn_height))
green = (47, 79, 79)
grey = (128, 128, 128)

def show_speed(speed):
    score_font = pygame.font.SysFont("bahnschrift", 25)
    speed_value = score_font.render('speed:' + str(speed), True, grey)
    scrn.blit(speed_value, [8, 30])


def your_snake(snake_block, snake_list):
    '''Snake'''
    for x in snake_list:
        pygame.draw.rect(scrn, green, [x[0], x[1], snake_block, snake_block])