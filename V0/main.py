import pygame
import random
from score import *
from menu import *
from show import *
pygame.init()

grey = (128, 128, 128)
orange = (255, 97, 3)
red = (213, 50, 80)
green = (47, 79, 79)
white = (255, 248, 220)
Gainsboro = (220, 220, 220)

scrn_width = 800
scrn_height = 600
scrn = pygame.display.set_mode((scrn_width, scrn_height))
pygame.display.set_caption('Snake Game')

pygame.mixer.init()
pygame.mixer.music.load("bgm.mp3", "r")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play()

snake_block = 10


def gameloop():
    '''Main Game'''
    quit = False
    game_over = False

    x1 = round(random.randrange(0, scrn_width - snake_block) / 10.0) * 10.0
    y1 = round(random.randrange(0, scrn_height - snake_block) / 10.0) * 10.0

    x1_change = 0
    y1_change = 0

    snake_list = []
    snake_length = 1


    food_x = round(random.randrange(0, scrn_width - snake_block) / 10.0) * 10.0
    food_y = round(random.randrange(0, scrn_height - snake_block) / 10.0) * 10.0
    pygame.display.update()

    while not quit:

        while game_over == True:
            show_end_screen(snake_length - 1)
            pygame.display.update()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -snake_block
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = snake_block


        if x1 >= scrn_width or x1 <= 0 or y1 >= scrn_height or y1 < 0:
            game_over = True

        snake_speed =  12 + snake_length//3
        clock = pygame.time.Clock()

        x1 += x1_change
        y1 += y1_change

        scrn.fill(white)
        size = 18
        scope_y = (0, scrn_height // size - 1)
        for x in range(size, scrn_width, size):
            pygame.draw.line(scrn, Gainsboro, (x, scope_y[0] * size), (x, scrn_height), 1)
        for y in range(scope_y[0] * size, scrn_height, size):
            pygame.draw.line(scrn, Gainsboro, (0, y), (scrn_width, y), 1)

        pygame.draw.rect(scrn, orange, [food_x, food_y, snake_block, snake_block])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_over = True

        your_snake(snake_block, snake_list)
        your_score(snake_length - 1)
        show_speed(snake_speed)

        pygame.display.update()

        if x1 == food_x and y1 == food_y:
            food_x = round(random.randrange(0, scrn_width - snake_block) / 10.0) * 10.0
            food_y = round(random.randrange(0, scrn_height - snake_block) / 10.0) * 10.0
            snake_length += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()


show_start_screen()