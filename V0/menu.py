import pygame_menu
from score import *

scrn_width = 800
scrn_height = 600
scrn = pygame.display.set_mode((scrn_width, scrn_height))

def show_start_screen():
    '''Main Menu'''
    from main import gameloop
    theme = pygame_menu.themes.THEME_DARK.copy()
    Munro = pygame_menu.font.FONT_MUNRO
    bit = pygame_menu.font.FONT_8BIT
    theme.widget_font = Munro
    theme.title_font = bit
    start_menu = pygame_menu.Menu(width=scrn_width, height=scrn_height, title='SNAKE GAME', theme=theme);
    if load_highscore() == 0:
        start_menu.add.label('There is no high score yet.')
    else:
        start_menu.add.label('High Score is ' + str(load_highscore()));
    
    start_menu.add.button("Play", gameloop);
    start_menu.add.button("Quit", pygame_menu.events.EXIT);
    start_menu.mainloop(scrn)


def replay_game():
    from main import gameloop
    gameloop()

def show_end_screen(score):
    '''Game Over Menu'''
    theme = pygame_menu.themes.THEME_DARK.copy()
    Munro = pygame_menu.font.FONT_MUNRO
    bit = pygame_menu.font.FONT_8BIT
    theme.widget_font = Munro
    theme.title_font = bit
    end_menu = pygame_menu.Menu(width=scrn_width, height=scrn_height, title='Game Over', theme=theme);
    if score > load_highscore():
        # New high score
        end_menu.add.label("New High Score! "+ "\n Your Score is " +str(score))
        save_high_score(score)
    else:
        end_menu.add.label("Your score is " + str(score));
    end_menu.add.button("Replay", replay_game);
    end_menu.add.button("Quit", pygame_menu.events.EXIT);
    end_menu.add.button("Main Menu", show_start_screen);
    end_menu.mainloop(scrn)

