import pygame

scrn_width = 800
scrn_height = 600
scrn = pygame.display.set_mode((scrn_width, scrn_height))

score_font = pygame.font.SysFont("bahnschrift", 25)
grey = (128, 128, 128)  # your_score, show_speed

player_name = '';
default_player_name = True;

def your_score(score):
    '''current player's score'''
    from menu import player_name
    value = score_font.render(player_name + "'s score:" + str(score), True, grey)
    scrn.blit(value, [8, 8])


def show_speed(speed):
    speed_value = score_font.render('speed:' + str(speed), True, grey)
    scrn.blit(speed_value, [8, 30])