from check_input_type import CheckInput
from difficulty_class import Set_Difficulty
from input_messages_class import InputMessages

user_input_valid = CheckInput()
set_difficulty = Set_Difficulty()

import random

class GameManager():
    def __init__(self):
        self.answer = 0
        self.guesses_left = None
        self.game_on = True
        #self.user_won = False


    def play_game(self, play_game):
        if play_game in ('y', 'yup', 'yes'):
            self.answer = random.randint(1, 100)
            print(self.answer)
            self.input_message = InputMessages()
            self.guesses_left = set_difficulty.difficulty_level()
            print("Ok, the computer challenges you to guess a number between 1 and 100...")
            self.guess_number()
        elif play_game in ('n', 'no', 'nope'):
            print("Ok, you don't want to play then... Bye, bye.")
        else:
            print("Your input was confusing, I assume you don't want to play then.")

        self.restart()


    def guess_number(self):
        while self.game_on and self.guesses_left >= 1:
            guess = input("Make a guess: ")
            if user_input_valid.check_user_input(guess):
                self.input_message.wait_time(self.guesses_left)
                guess = int(guess)
                if guess == self.answer:
                    print("THAT'S THE CORRECT ANSWER!")
                    self.game_on = False
                else:
                    self.input_message.user_hint(self.answer, guess)
            
            self.guesses_left -= 1


    def restart(self):
        restart = input("Would you like to erase the computer's memory and restart the game? 'yes' or 'no': ")
        if restart in ('y', 'yup', 'yes'):
            self.game_on = True
            self.play_game(play_game="yes")
        elif restart in ('n', 'no', 'nope'):
            print("Ok, I'll quit the program then. Goodbye.")
        else:
            print("Your input was confusing. Therefore I'll end the whole program.")


if __name__ == "__main__":
    game = GameManager()
    play_game = str(input("Do you want to play? 'yes' or 'no': ")).lower()
    game.play_game(play_game)
