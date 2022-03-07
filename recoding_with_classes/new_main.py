from telnetlib import GA
from check_input_type import CheckInput

user_input_valid = CheckInput()

import random

class GameManager():
    def __init__(self):
        self.play = None
        self.answer = random.randint(1, 100)

    
    def play_game(self):
        self.play = str(input("Do you want to play a game? 'yes' or 'no': ")).lower()
        if self.play in ('y', 'yup', 'yes'):
            pass
        else:
            pass


    def stuff(self):
        guess = input("Make a guess: ")
        if user_input_valid.check_user_input(guess):
            print("Input value: VALID")
        else:
            print("Input value: NOT VALID")


if __name__ == "__main__":
    GameManager()
