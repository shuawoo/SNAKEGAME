import pygame
import random
import pygame_menu
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

player_name = '';
default_player_name = True;

snake_block = 10

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("bahnschrift", 25)


def load_highscore():
    '''High Score_Score'''

    try:
        high_score_file = open("highscore.txt", "r")
        high_score = int(high_score_file.read())
        high_score_file.close()
    except:
        high_score = 0

    return high_score


def load_bestplayer():
    '''High Score_Player'''
    try:
        best_player_file = open("bestplayer.txt", "r")
        best_player = str(best_player_file.read())
        best_player_file.close()
    except:
        best_player = ''

    return best_player


def save_high_score(new_high_score):
    # Write the high score file
    high_score_file = open("highscore.txt", "w")
    high_score_file.write(str(new_high_score))
    high_score_file.close()


def save_best_player(player):
    # Write the high score file
    best_player_file = open("bestplayer.txt", "w")
    best_player_file.write(str(player))
    best_player_file.close()


def set_player_name(name):
    '''Player Name'''
    global player_name;
    global default_player_name;
    player_name = name;
    default_player_name = False;


def set_default_player_name():
    '''Default Player Name'''
    global player_name;
    global default_player_name;
    player_name = "Guest"
    default_player_name = False


theme = pygame_menu.themes.THEME_DARK.copy()
Munro = pygame_menu.font.FONT_MUNRO
bit = pygame_menu.font.FONT_8BIT
theme.widget_font = Munro
theme.title_font = bit


def show_start_screen():
    '''Main Menu'''
    start_menu = pygame_menu.Menu(width=scrn_width, height=scrn_height, title='SNAKE GAME', theme=theme);
    if load_highscore() == 0:
        start_menu.add.label('There is no high score yet.')
    else:
        start_menu.add.label('High Score is ' + str(load_highscore()) + " by " + str(load_bestplayer()));
    start_menu.add.text_input("Your Name: ", default="Guest", onchange=set_player_name);
    start_menu.add.button("Play", gameloop);
    start_menu.add.button("Quit", pygame_menu.events.EXIT);
    if default_player_name:
        set_default_player_name();
    start_menu.mainloop(scrn)


def replay_game():
    gameloop()


def your_score(score):
    '''current player's score'''
    value = score_font.render(player_name + "'s score:" + str(score), True, grey)
    scrn.blit(value, [8, 8])


def show_speed(speed):
    speed_value = score_font.render('speed:' + str(speed), True, grey)
    scrn.blit(speed_value, [8, 30])


def show_end_screen(score):
    '''Game Over Menu'''
    end_menu = pygame_menu.Menu(width=scrn_width, height=scrn_height, title='Game Over', theme=theme);
    if score > load_highscore():
        # New high score
        end_menu.add.label("New High Score! "+ "*" + player_name + "*" + "\n Your Score is " +str(score))
        save_high_score(score)
        save_best_player(player_name)
    else:
        end_menu.add.label(player_name + "! Your score is " + str(score));
    end_menu.add.button("Replay", replay_game);
    end_menu.add.button("Quit", pygame_menu.events.EXIT);
    end_menu.add.button("Main Menu", show_start_screen);
    end_menu.mainloop(scrn)


# i want head black #head and body different color
def your_snake(snake_block, snake_list):
    '''Snake'''
    for x in snake_list:
        pygame.draw.rect(scrn, green, [x[0], x[1], snake_block, snake_block])


def gameloop():
    '''Main Game'''
    game_over = False
    game_close = False
    # ！！ can have x2 y2  ！！don't show up too close to the boundary?
    x1 = round(random.randrange(0, scrn_width - snake_block) / 10.0) * 10.0
    y1 = round(random.randrange(0, scrn_height - snake_block) / 10.0) * 10.0

    x1_change = 0
    y1_change = 0

    snake_list = []
    snake_length = 1  # define the score

    # !! not in the position of the snake?
    food_x = round(random.randrange(0, scrn_width - snake_block) / 10.0) * 10.0
    food_y = round(random.randrange(0, scrn_height - snake_block) / 10.0) * 10.0
    pygame.display.update()

    while not game_over:

        while game_close == True:
            show_end_screen(snake_length - 1)
            pygame.display.update()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
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

        #  !! diffenrent color bound
        if x1 >= scrn_width or x1 <= 0 or y1 >= scrn_height or y1 < 0:
            game_close = True

        snake_speed =  12 + snake_length//3
        clock = pygame.time.Clock()


        x1 += x1_change
        y1 += y1_change

        scrn.fill(white)
        size = 18
        scope_x = (0, scrn_width // size - 1)
        scope_y = (0, scrn_height // size - 1)
        for x in range(size, scrn_width, size):
            pygame.draw.line(scrn, Gainsboro, (x, scope_y[0] * size), (x, scrn_height), 1)
        for y in range(scope_y[0] * size, scrn_height, size):
            pygame.draw.line(scrn, Gainsboro, (0, y), (scrn_width, y), 1)

        pygame.draw.rect(scrn, orange, [food_x, food_y, snake_block, snake_block])  # different color and limit position
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

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
