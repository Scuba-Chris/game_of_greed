from random import shuffle
from collections import Counter

class Game:

    def __init__(self):
        pass
        # self.name = name

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

if __name__ == "__main__":
    play = Game()