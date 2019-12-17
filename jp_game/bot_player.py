""""
Create a Game of Greed Player Bot
ONLY use public methods
- Game class constructor
- play
- calculate_score
"""
from collections import Counter
# from jb_game_of_greed import calculate_score
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
        self.counter = Counter

    def _print(self, *args):
        
        msg = args[0]

        if msg.startswith('You rolled'):
            self.roll = [int(char) for char in msg if char.isdigit()]

        # print(msg)

    def keep_straight(self, counter):
        return ''.join([str(d) for d in self.roll if len(counter) == 6])

    def keep_three_pairs(self, counter):
        return ''.join([str(d) for d in self.roll if self.counter])

    def keep_triples(self, counter):
        return ''.join([str(d) for d in self.roll if self.counter])
    
    def keep_ones(self, counter):
        return ''.join([str(d) for d in self.roll if d == 1])

    def keep_fives(self, counter):
        return ''.join([str(d) for d in self.roll if d == 5])

    def dice_to_keep(self):

        counter = Counter(self.roll)

        if len(counter) == 6:
            return self.keep_straight(counter)
        
        elif len(counter) == 3 and counter.most_common()[2][1] == 2:
            return self.keep_three_pairs(counter)

        elif counter.key > 3 and value = 3:
            return
            
        elif 1 in self.roll:
            return self.keep_ones(counter)

        elif 5 in self.roll:
            return self.keep_fives(counter)

        return ''
     
    def roll_again(self):
        if len(self.roll) > 3:
            return 'y'
        else:
            return 'n'

    def _input(self, *args):
        prompt = args[0]

        if prompt == 'Wanna play? ':
            # print(prompt,'y')
            return 'y'

        if prompt == 'Enter dice to keep: ':
            response_str = self.dice_to_keep()
            return response_str




if __name__ == "__main__":
    bot = YesBot()
    game = Game(bot._print, bot._input)
    bot.game = game
    game.play(10)
    play = 10000

    high_score = 0
    low_score = 10000
    avg_score = 0
    total_score = 0

    for _ in range(play):
        total_score += game.score
        if game.score > high_score:
            high_score = game.score
        if game.score < low_score:
            low_score = game.score
        avg_score = total_score / play
        game.play()

    print('')
    print(f'high score {high_score}')
    print(f'low score {low_score}')
    print(f'avg score {avg_score}')