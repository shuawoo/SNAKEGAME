import pygame
import pygame_menu
from score import *

pygame.init()

scrn_width = 800
scrn_height = 600
scrn = pygame.display.set_mode((scrn_width, scrn_height))

score_font = pygame.font.SysFont("bahnschrift", 25)

grey = (128, 128, 128)  # your_score, show_speed

theme = pygame_menu.themes.THEME_DARK.copy()
Munro = pygame_menu.font.FONT_MUNRO
bit = pygame_menu.font.FONT_8BIT
theme.widget_font = Munro
theme.title_font = bit

player_name = '';
default_player_name = True;

def set_default_player_name():
    '''Default Player Name'''
    global player_name;
    global default_player_name;
    player_name = "Guest"
    default_player_name = False

def set_player_name(name):
    '''Player Name'''
    global player_name;
    global default_player_name;
    player_name = name;
    default_player_name = False;
    

def show_start_screen():
    '''Main Menu'''
    from main import gameloop
    start_menu = pygame_menu.Menu(width=scrn_width, height=scrn_height, title='SNAKE GAME', theme=theme);
    if load_high_score() == {'top1': ['', '0'], 'top2': ['', '0'], 'top3': ['', '0']}:
        start_menu.add.label('There is no high score yet.');
        start_menu.add.text_input("Your Name: ", default="Guest", onchange=set_player_name);
        start_menu.add.button("Play", gameloop);
        start_menu.add.button("Quit", pygame_menu.events.EXIT);
    else:
        start_menu.add.label('High Score is ' + str(load_high_score()['top1'][1]) + " by " + str(load_high_score()['top1'][0]));
        start_menu.add.text_input("Your Name: ", default="Guest", onchange=set_player_name);
        start_menu.add.button("Play", gameloop);
        start_menu.add.button("Hall of Fame", show_highscore);
        start_menu.add.button("Quit", pygame_menu.events.EXIT);

    if default_player_name:
        set_default_player_name();
    start_menu.mainloop(scrn)

def show_highscore():
    '''Hall of Fame'''
    hs_menu = pygame_menu.Menu(width=scrn_width, height=scrn_height, title='SNAKE GAME', theme=theme);
    hs_menu.add.label("Hall of Fame")
    scores = load_high_score()
    n = 1
    for i in scores:
        if int(scores.get(i)[1])>0:
            hs_menu.add.label(str(n)+ ". "+ str(scores[i][0]) + "    *" + str(scores[i][1]) +"*")
        n += 1
    hs_menu.add.button("Main Menu", show_start_screen);
    hs_menu.add.button("Quit", pygame_menu.events.EXIT);
    hs_menu.mainloop(scrn)

def replay_game():
    from main import gameloop
    gameloop()

def show_end_screen(score):
    '''Game Over Menu'''
    end_menu = pygame_menu.Menu(width=scrn_width, height=scrn_height, title='Game Over', theme=theme);
    scores = load_high_score()
    if score > int(scores['top1'][1]):
        end_menu.add.label("You are the best player! "+ "*" + player_name + "*" + "\n Your Score is " +str(score))
        set_high_score(player_name, score)
    elif score > int(scores['top2'][1]):
        end_menu.add.label("New High Score! "+ "*" + player_name + "*" + "\n Your Score is " +str(score))
        set_high_score(player_name, score)
    elif score > int(scores['top3'][1]):
        end_menu.add.label("New High Score! "+ "*" + player_name + "*" + "\n Your Score is " +str(score))
        set_high_score(player_name, score)
    elif score == 0:
        end_menu.add.label("Try Again " + player_name + "\n Your Score is " + str(score));
    else:
        end_menu.add.label(player_name + "! Your score is " + str(score));
    end_menu.add.button("Replay", replay_game);
    end_menu.add.button("Quit", pygame_menu.events.EXIT);
    end_menu.add.button("Main Menu", show_start_screen);
    end_menu.mainloop(scrn)


