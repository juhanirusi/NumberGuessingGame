class CheckInput:
    def check_user_input(self, guess):
        try:
            guess = int(guess)
        except ValueError:
            try:
                guess = float(guess)
            except ValueError:
                guess = str(guess)
        finally:
            if self.check_input_type(guess):
                return True
            else:
                return False


    def check_input_type(self, guess):
        if type(guess) == float:
            print("You inputted a float number, it NEEDS TO BE AN INTEGER! Try again...")
        elif type(guess) == str:
            print("You inputted a string, it NEEDS TO BE AN INTEGER! Try again...")
        elif type(guess) == int:
            if guess > 100:
                print("Well now you're going WAY over the roof. I can't take this to the computer when it explicitly said NUMBER BETWEEN 1 AND 100!")
            elif guess < 1:
                print("Your guess is WAY too low. I can't take this to the computer when it explicitly said NUMBER BETWEEN 1 AND 100!")
            else:
                return True

        return False
