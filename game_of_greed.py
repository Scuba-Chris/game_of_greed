import random
from collections import Counter
import re


class Game:

    def __init__(self, _print=print, _input=input):
        self._print = print
        self._input = input
        # self._roll_dice = roll_dice 
        self._round_num = 10
        self._score = 0
        self.rolled = []
        self.keepers = []

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
    
    def roll_dice(self, num_dice):
        
        return [random.randint(1,6) for i in range(num_dice)]

    def dice_handling(self, num_dice=6):
        selected_dice = ()
        self.rolled = self.roll_dice(num_dice) 
        selected_dice = tuple(int(char) for char in self.keepers)
        self._print(selected_dice)
    
    def dice_inputs(self, message):
        while True:
            try:
                user_input = self._input(message)
                user_input = [int(num) for num in user_input]
                for num in user_input:   
                    if 1 > num or num > 6:
                        raise ValueError('please enter 1 -6')
                # regex_obj = re.compile(r'[1-6]{1-6}')
                # match_obj = regex_obj.match(user_input)
            except ValueError:
                self._print('Please only enter numbers')
                continue
            else:
                return user_input

    def play(self):

        self._print('welcome to game of greed!')
        start_awnser = self._input('are you ready to play? - ')
        if start_awnser == 'y':
            self.dice_handling()
            self._print(self.rolled)
            held_dice_returned_str = (self.dice_inputs('what numbers would you like to keep? - '))
            # held_dice = re.findall(r'[1-6]{1,6}', str)
            self.keepers.append(held_dice_returned_str) 
        else:
            self._print('ok. maybe another time')




if __name__ == "__main__":
    game = Game()

    game.play()
    game.dice_handling()
    # try:
    #     game.calculate_score(dice)
    #     print(game.roll_dice(6))
    # except:
    #     print('well then')
