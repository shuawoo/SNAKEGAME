import pygame

score_font = pygame.font.SysFont("bahnschrift", 25)
grey = (128, 128, 128)  # your_score, show_speed

def your_score(score):
    '''current player's score'''
    from menu import player_name
    from main import scrn
    value = score_font.render(player_name + "'s score:" + str(score), True, grey)
    scrn.blit(value, [8, 8])


def show_speed(speed):
    from main import scrn
    speed_value = score_font.render('speed:' + str(speed), True, grey)
    scrn.blit(speed_value, [8, 30])