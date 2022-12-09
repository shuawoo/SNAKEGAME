import pygame 

def load_highscore():
    '''High Score_Score'''

    try:
        high_score_file = open("highscore.txt", "r")
        high_score = int(high_score_file.read())
        high_score_file.close()
    except:
        high_score = 0

    return high_score

def save_high_score(new_high_score):
    # Write the high score file
    high_score_file = open("highscore.txt", "w")
    high_score_file.write(str(new_high_score))
    high_score_file.close()

def your_score(score):
    '''current player's score'''
    from main import scrn
    grey = (128, 128, 128)
    score_font = pygame.font.SysFont("bahnschrift", 25)
    value = score_font.render("Your score is:" + str(score), True, grey)
    scrn.blit(value, [8, 8])