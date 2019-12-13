""""
Create a Game of Greed Player Bot
ONLY use public methods
- Game class constructor
- play
- calculate_score
"""
from collections import Counter
from jb_game_of_greed import Game

class LazyPlayer:
    # constructor, play and calcuate_score available
    # everything else is done only with I/O
    def __init__(self):
        self.roll = None

    def _print(self, *args):
        print(args[0])

    def _input(self, *args):
        print(args[0], 'n')
        return 'n'


class ParticipationTrophyPlayer:

    def __init__(self):
        self.roll = None
        self.game = None

    def _print(self, *args):

        msg = args[0]

        if msg.startswith('You rolled'):
            self.roll = [int(char) for char in msg if char.isdigit()]

        print(msg)

    def _input(self, *args):
        prompt = args[0]

        if prompt == 'Wanna play? ':
            print(prompt,'y')
            return 'y'

        if prompt == 'Roll again? ':
            print(prompt, 'n')
            return 'n'

        if prompt == 'Enter dice to keep: ':
            print(prompt)

            # You'll want to figure out which dice you want to keep
            # by calculating the score
            # score = self.game.calculate_score(self.roll)

            # conver the entire roll back to string
            # e.g. [1,1,5] to '115'
            response_str = ''
            for val in self.roll:
                response_str += str(val)

            # this demo is responding with string that includes
            # non-scoring dice
            # this is a bug, but does not affect this bot
            # since the bot never re-rolls
            return response_str

class YesBot:
    def __init__(self):
        self.roll = None
        self.game = None

    def _print(self, *args):
        
        msg = args[0]

        if msg.startswith('You rolled'):
            self.roll = [int(char) for char in msg if char.isdigit()]

        print(msg)

    def keep_straight(self):
        return ''.join([str(d) for d in self.roll if d == 123456])

    

    
    def roll_pairs(self, count):
        pass

    def dice_to_keep(self):
        return ''.join([str(d) for d in self.roll if d == 1])
     

    def _input(self, *args):
        prompt = args[0]

        if prompt == 'Wanna play? ':
            print(prompt,'y')
            return 'y'

        if prompt == 'Enter dice to keep: ':
            response_str = self.dice_to_keep()
            return response_str

        while 



if __name__ == "__main__":
    bot = YesBot()
    game = Game(bot._print, bot._input)
    bot.game = game
    game.play(10)
