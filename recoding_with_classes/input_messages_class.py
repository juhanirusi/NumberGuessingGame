import time
from user_hints_class import UserHints

user_hints = UserHints()

FAMOUS_NUMBERS = {8, 99}

class InputMessages(UserHints):
    def __init__(self):
        self.user_guesses = 0
        self.run_once = True
        super().__init__()


    def wait_time(self, guesses_left):
        self.user_guesses += 1
        time.sleep(0.7)

        if self.user_guesses == 3:
            print("""\nOk, they say "the third time is the charm", so let's see if it's true...\n""")
        elif self.user_guesses == 2:
            print("\nOk, let me check your second guess, just wait a second...\n")
        elif self.user_guesses == 1:
            print("\nOk, let me check...\n")
        else:
            print("\nJust a second...\n")
        if guesses_left == 1:
            time.sleep(1)
            print("Drumroll please \U0001F941\U0001F941\U0001F941\U0001F941\U0001F941...\n")
            time.sleep(1)

        time.sleep(2)


    def user_hint(self, answer, guess):
        if self.user_guesses == 1:
            user_hints.user_hint_1(answer, guess)
        elif self.user_guesses == 2:
            user_hints.user_hint_2(answer, guess)
        else:
            user_hints.user_hint_3(answer, guess)

        if self.run_once:
            if answer in FAMOUS_NUMBERS:
                self.run_once = False
                user_hints.famous_number_hint(answer)


    def game_over(self):
        pass