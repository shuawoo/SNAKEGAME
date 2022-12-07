import pygame
import random
import pygame_menu

pygame.init()

grey = (128, 128, 128)  # your_score, show_speed,
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


class Point:
    row = 0
    col = 0
    def __init__(self, row, col):
        self.row = row
        self.col = col
    def copy(self):
        return Point(row=self.row, col=self.col)


def rect(point, color):
    cell = scrn_width / COL
    left = point.col * cell
    top = point.row * cell
    pygame.draw.rect(scrn, color, (left, top, cell, cell))


pygame.mixer.init()
pygame.mixer.music.load("bgm.mp3", "r")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play()
sound_eat = pygame.mixer.Sound("sound_eat.wav")
sound_eat.set_volume(1)
sound_gameover = pygame.mixer.Sound("sound_gameover.wav")
sound_gameover.set_volume(1)

player_name = '';
default_player_name = True;

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("bahnschrift", 25)


def load_high_score():
    #Load High Score from txt file
    scores = ""
    try:
        high_score_file = open("high_score.txt", "r")
        scores = high_score_file.read()
        high_score_file.close()
    except:
        high_score_file = open("high_score.txt", "w")
        scores = "top1::0,top2::0,top3::0"
        high_score_file.write(scores)
        high_score_file.close()

    score_list = scores.split(',')

    to_return = {}
    
    for element in score_list: 
        l = element.split(':')
        to_return[l[0]] = [l[1], l[2]]

    return to_return


def save_high_score(scores):
    # Write the high score file
    high_score_file = open("high_score.txt", "w")
    to_write = ""
    for i in scores: 
        to_write += i
        to_write += ':'
        to_write += str(scores.get(i)[0])
        to_write += ':'
        to_write += str(scores.get(i)[1])
        to_write += ','
    to_write = to_write[:-1]
    high_score_file.write(to_write)
    high_score_file.close()
    print(to_write)

def set_high_score(player_name, score):
    scores = load_high_score()
    '''Save Player score as top1, top2, or top3'''
    if (score > int(scores.get('top1')[1])):
        scores['top3'][0] = str(scores.get('top2')[0])
        scores['top3'][1] = int(scores.get('top2')[1]) 
        scores['top2'][0] = str(scores.get('top1')[0])
        scores['top2'][1] = int(scores.get('top1')[1])
        scores['top1'][0] = player_name
        scores['top1'][1] = score
    elif (score > int(scores.get('top2')[1])):
        scores['top3'][0] = str(scores.get('top2')[0])
        scores['top3'][1] = int(scores.get('top2')[1])
        scores['top2'][0] = player_name
        scores['top2'][1] = score
    elif (score > int(scores.get('top3')[1])):
        scores['top3'][0] = player_name
        scores['top3'][1] = score

    save_high_score(scores)


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