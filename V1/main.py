import pygame
import random
from draw import *
from score import *
from menu import *

pygame.init()

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("bahnschrift", 25)

orange = (255, 97, 3)  # food
red = (213, 50, 80)  # not used
green = (47, 79, 79)  # not used
white = (255, 248, 220)  # scrn
Gainsboro = (220, 220, 220)  # lines
black = (0, 0, 0)  # snake head
gold = (255, 215, 0)  # snake body

scrn_width = 800
scrn_height = 600
ROW = 60
COL = 80
cell = scrn_width / COL
scrn = pygame.display.set_mode((scrn_width, scrn_height))
pygame.display.set_caption('Snake Game')

pygame.mixer.init()
pygame.mixer.music.load("bgm.mp3", "r")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play()
sound_eat = pygame.mixer.Sound("sound_eat.wav")
sound_eat.set_volume(1)
sound_gameover = pygame.mixer.Sound("sound_gameover.wav")
sound_gameover.set_volume(1)

def your_score(score):
    '''current player's score'''
    value = score_font.render(player_name + "'s score:" + str(score), True, grey)
    scrn.blit(value, [8, 8])


def show_speed(speed):
    speed_value = score_font.render('speed:' + str(speed), True, grey)
    scrn.blit(speed_value, [8, 30])


def gameloop():
    '''Main Game'''
    quit = False
    game_over = False
    direct = "left"
    head = Point(row=random.randint(0, ROW - 1), col=random.randint(COL / 2, COL - 1))
    body = [Point(row=head.row, col=head.col + 1), Point(row=head.row, col=head.col + 2)]
    score = len(body) - 2

    fruit = Point(row=random.randint(0, ROW - 1), col=random.randint(0, COL - 1))

    while not quit:

        if game_over == True:
            sound_gameover.play()
            show_end_screen(score)
            pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    direct = "left"
                elif event.key == pygame.K_RIGHT:
                    direct = "right"
                elif event.key == pygame.K_UP:
                    direct = "up"
                elif event.key == pygame.K_DOWN:
                    direct = "down"


        eat = (head.row == fruit.row and head.col == fruit.col)
        if eat:
            sound_eat.play()
            fruit = Point(row=random.randint(0, ROW - 1), col=random.randint(0, COL - 1))
            score += 1
        body.insert(0, head.copy())
        if not eat:
            body.pop()

        if direct == "left":
            head.col -= 1
        elif direct == "right":
            head.col += 1
        elif direct == "up":
            head.row -= 1
        elif direct == "down":
            head.row += 1


        scrn.fill(white)
        size = 18
        scope_x = (0, scrn_width // size - 1)
        scope_y = (0, scrn_height // size - 1)
        for x in range(size, scrn_width, size):
            pygame.draw.line(scrn, Gainsboro, (x, scope_y[0] * size), (x, scrn_height), 1)
        for y in range(scope_y[0] * size, scrn_height, size):
            pygame.draw.line(scrn, Gainsboro, (0, y), (scrn_width, y), 1)

        for snake in body:
            rect(snake, gold)
        rect(head, black)
        rect(fruit, orange)


        if head.col < 0 or head.col > COL or head.row < 0 or head.row > ROW:
            game_over = True
        for snake in body:
            if head.col == snake.col and head.row == snake.row:
                game_over = True

        snake_speed = 12 + score // 3
        clock = pygame.time.Clock()

        your_score(score)
        show_speed(snake_speed)
        pygame.display.update()
        clock.tick(snake_speed)

    pygame.quit()
    quit()


show_start_screen()