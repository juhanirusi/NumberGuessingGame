class CheckAnswer:
    def __init__(self, correct_answer, guess):
        self.answer = correct_answer
        self.guess = guess


    def check_user_input(self, guess):
        try:
            guess = int(guess)
        except ValueError:
            try:
                guess = float(guess)
            except ValueError:
                guess = str(guess)
        finally:
            self.check_input_type(guess)


    def check_input_type(self, guess):
        if type(guess) == float:
            return "You inputted a float number, it NEEDS TO BE AN INTEGER! Try again..."
        elif type(guess) == str:
            return "You inputted a string, it NEEDS TO BE AN INTEGER! Try again..."
