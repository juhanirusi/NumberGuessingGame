class CheckInput:
    """
    This class is used to check the type of input user used for
    guessing the number and show appropriate messages based on that input.
    """

    def check_user_input(self, guess):
        """
        Checks the type of input user used and shows a message
        to the user if the input data type isn't an integer or
        between the predefined range (e.g. 0-100)

        Lastly, returns a boolean depending on the result of the input type.
        """
        try:
            guess = int(guess)
            if guess > 100:
                print("Well now you're going WAY over the roof. I can't take this to the computer when it explicitly said NUMBER BETWEEN 1 AND 100!")
            elif guess < 1:
                print("Your guess is WAY too low. I can't take this to the computer when it explicitly said NUMBER BETWEEN 1 AND 100!")
            else:
                return True
        except ValueError:
            try:
                guess = float(guess)
                print("You inputted a float number, it NEEDS TO BE AN INTEGER! Try again...")
            except ValueError:
                guess = str(guess)
                print("You inputted a string, it NEEDS TO BE AN INTEGER! Try again...")

        return False
