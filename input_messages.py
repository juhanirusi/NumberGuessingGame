import time

def wrong_game_input(wrong_game_inputs):
    """
    If the user inputs something else than 'yes' or 'no' to the play_game input these messages are shown
    """
    if wrong_game_inputs == 1:
        print("That's a wrong input, I can't forward this to the computer. perhaps you made a typo? \U0001F92D Try again...")
    elif wrong_game_inputs == 2:
        print("Well, now your playing games with me. \U0001F612 Try again...")
    elif wrong_game_inputs == 3:
        print("Ok now I'm getting annoyed, \U0001F624 mess with me again, and I'll end the game....")
    else:
        pass


def does_user_want_to_play(play_game):
    """
    When the user inputs 'no' for the last time i.e. doesn't want to play, this message is shown...
    """
    
    if play_game == "no":
        print("Oops, now you hurt the computer's feelings and it decided to leave to count zeros and ones.")
        print("However, the computer left one last message to you, but apparently it got so mad that it didn't bother to translate it completely...\n")
        print("You are such a 01110000 01100001 01110010 01110100 01111001 00100000 01110000 01101111 01101111 01110000 01100101 01110010, and I never wanna play with you again!")
        print("...I have no idea what that means, \U0001F914 but the computer isn't happy. \U0001F620 \n")
    else:
        pass
        

def user_guessed_number(user_guess):
    if user_guess > 100:
        print("Well now you're going WAY over the roof. I can't take this to the computer when it explicitly said NUMBER BETWEEN 1 AND 100!")
    elif user_guess < 1:
        print("Your guess is WAY too low. I can't take this to the computer when it explicitly said NUMBER BETWEEN 1 AND 100!")
    else:
        pass


def check_user_input(guess):
    
    user_guess = input(guess)
    
    try:
        result = int(user_guess)
    except ValueError:
        try:
            result = float(user_guess)
        except ValueError:
            result = str(user_guess)
    finally:
        return result


def wait_time(guesses, guesses_left):
    time.sleep(0.7)

    if guesses == 3:
        print("""\nOk, they say "the third time is the charm", so let's see if it's true...\n""")
    elif guesses == 2:
        print("\nOk, let me check your second guess, just wait a second...\n")
    elif guesses == 1:
        print("\nOk, let me check...\n")
    else:
        print("\nJust a second...\n")
    if guesses_left == 0:
        time.sleep(1)
        print("Drumroll please \U0001F941\U0001F941\U0001F941\U0001F941\U0001F941...\n")
        time.sleep(1)

    time.sleep(2)