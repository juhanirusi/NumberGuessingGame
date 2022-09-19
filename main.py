import random

from check_input_type import CheckInput
from difficulty import Set_Difficulty
from messages import InputMessages

user_input_valid = CheckInput()
set_difficulty = Set_Difficulty()


class GameManager():
    """
    Our game manager class that is responsible for starting the
    game, keeping the game on, restarting the game if the user wants
    to, and calling the appropriate methods to calculate whether the
    user can still play the game and show messages to the user depending
    on the user inputs.
    """

    def __init__(self):
        """"Our init that holds the variables needed throughout the game"""
        self.answer = 0
        self.guesses_left = None
        self.game_on = True

    def play_game(self, play_game):
        """
        A method we call when the game starts the first
        time that starts or ends the game based on the user
        input and after the game is over, calls the restart method.
        """
        self.input_message = InputMessages()

        if play_game in ('y', 'yup', 'yes', 'yeah'):
            self.answer = random.randint(1, 100)
            print(self.answer)
            self.guesses_left = set_difficulty.difficulty_level()
            print(
                "Ok, the computer challenges you to guess a number between 1 and 100...")
            self.guess_number()
        elif play_game in ('n', 'no', 'nope', 'no way'):
            print("Okay, I understand, see you next time.")
        else:
            print("Your input was confusing, I assume you don't want to play then.")

        self.restart()

    def guess_number(self):
        while self.game_on:

            self.input_message.guesses_left_message(self.guesses_left)

            self.guesses_left -= 1
            guess = input("Make a guess: ")
            #print(self.guesses_left)

            if user_input_valid.check_user_input(guess) and self.guesses_left >= 0:
                self.input_message.wait_time(self.guesses_left)

                if int(guess) == self.answer:
                    print(f"YES! YOU'RE RIGHT, THE ANSWER WAS: {self.answer}")
                    break
                elif guess != self.answer and self.guesses_left > 0:
                    self.input_message.user_hint(self.answer, guess)

            if self.guesses_left == 0:
                print("Oh no, you've ran out of guesses and therefore, lost the game.")
                print(f"The answer we were looking for was: {self.answer}")
                print("Better luck next time!")
                break

    def restart(self):
        """
        Is used to restart the game when the game is over,
        it gives the user a chance to restart the game or
        end it based on their input.
        """
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
