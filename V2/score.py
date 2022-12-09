def load_high_score():
    # Load High Score from txt file
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
