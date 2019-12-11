from random import shuffle
from collections import Counter


class Game:

    def __init__(self):
        pass

    def play(self):

        print('welcome to game of greed!')

        while True:
            start_awnser = input('are you ready to play?')
            if start_awnser == 'y':
                print('check back tomorrow')
                break
            else:
                print('ok. maybe another time')
                break

    def calculate_score(self, dice):
        
        roll_counter = Counter(dice)
        while True:
            score_count = 0
            if len(roll_counter) > 0:
                if len(roll_counter) == 6:
                    return 1500
                elif len(roll_counter) == 3 and roll_counter.most_common()[2][1] == 2:
                    return 1500
                for key, value in roll_counter.items():
                    if roll_counter[5] == 4 and roll_counter[1] == 2:
                        score_count += 2000        
                    elif key == 1 and value == 6:
                        score_count += 4000
                    elif key == 1 and value == 5:
                        score_count += 3000
                    elif key == 1 and value == 4:
                        score_count += 2000
                    elif key == 1 and value == 3:
                        score_count += 1000
                    elif key >= 2 and value == 3:
                        score_count += (key)*100
                    elif key >= 2 and value == 4:
                        score_count += (key)*200
                    elif key >= 2 and value == 5:
                        score_count += (key)*300
                    elif key >= 2 and value == 6:
                        score_count += (key)*400
                    elif key == 1 and value <= 2:
                        score_count += (value)*100
                    elif key == 5 and value < 3:
                        score_count += (value)*50
                roll_counter.popitem()
            else:
                break 
            return score_count 
        return 0

if __name__ == "__main__":
    game = Game()

    try:
        game.play()
        game.calculate_score(dice)

    except:
        print('well then')
