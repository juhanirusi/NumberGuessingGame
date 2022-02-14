import random
import user_hints
import difficulty
import input_messages

# Try to add an user interface to this project...
# https://docs.python.org/3/library/tkinter.html
# Google --> "adding user interface in python"

def game():

    answer = random.randint(1, 100)

    print("\nThe computer generated this number:", answer, "\n")

    # TODO Run only once --> AFTER RESTARTING DON'T RUN THIS CODE!
    play_game = str(input("Do you want to play a game? 'yes' or 'no': ")).lower()

    difficulty_not_set = True
    wrong_game_inputs = 0
    user_plays_game = True
    first_no_input = True
    first_guess = True
    user_hint = 0
    guesses = 0

    def restart():
        """
        The function for restarting the program (if the user wants to).
        """

        global user_plays_game

        restart = input("Would you like to restart the game, and erase the computer's memory? ")
        if restart in ('y', 'yup', 'yes'):
            game()
        elif restart in ('n', 'no', 'nope'):
            user_plays_game = False
            print("Ok, I'll quit the program. Goodbye.")
        else:
            user_plays_game = False
            print("Your input was confusing. Therefore I'll end the whole program.")

    while user_plays_game:
        if play_game in ('y', 'yup', 'yes'):
            if difficulty_not_set:
                guesses_left = difficulty.difficulty_level("Choose a difficulty. Type 'easy', 'medium' or 'hard': ")
                difficulty_not_set = False

            if first_guess:
                user_guess = input_messages.check_user_input("Ok, the computer challenges you to guess a number between 1 and 100: ")
                first_guess = False
            else:
                if guesses_left == 1:
                    print(f"You only have {guesses_left} attempt remaining. MAKE IT COUNT!")
                elif guesses_left > 1:
                    print(f"You have still {guesses_left} attempts remaining to guess the right number.")
                user_guess = input_messages.check_user_input("\nGuess again: ")

            guesses_left -= 1
            guesses += 1

            if guesses_left <= 0 and user_guess != answer:
                print("\nOh no, you've ran out of guesses, and therefore, lost the game. \U0001F61E")
                restart()
                break

            if type(user_guess) == int:
                input_messages.user_guessed_number(user_guess)
                if user_guess != answer and user_guess < 100 and user_guess > 0:
                    user_hint += 1
                    if user_hint == 1:
                        user_hints.user_hint_1(answer, user_guess)
                    elif user_hint == 2:
                        user_hints.user_hint_2(answer, user_guess)
                    elif user_hint == 3 and answer >= 10:
                        user_hints.user_hint_3(answer)
                elif user_guess == answer:
                    print(f"\nCONGRATULATIONS! You guessed the number right it was {answer}. The computer praises you! \U0001F64C")
                    if guesses == 1:
                        print(f"You got the number right with your first guess. THAT'S ASTONISHING, even the computer is amazed \U0001F632 \n")
                    else:
                        print(f"You got the number right with {guesses} guesses. GOOD JOB!\n")
                    print("The computer had one last message to you, but I wasn't able to translate it completely...")
                    print('"You are such a 01100110 01110101 01101110 person!" ...Whatever that means? \U0001F914\n')
                    restart()
                    break

            else:
                if type(user_guess) == float:
                    print("You inputted a float number, it NEEDS TO BE AN INTEGER! Try again...")
                elif type(user_guess) == str:
                    print("You inputted a string, it NEEDS TO BE AN INTEGER! Try again...")

        elif play_game in ('n', 'no', 'nope'):
            if first_no_input:
                play_game = str(input("Are you sure? The computer REALLY wants to play with you: ")).lower()
                first_no_input = False
            input_messages.does_user_want_to_play(play_game)
            if play_game in ('n', 'no', 'nope'):
                print("GAME OVER")
                restart()
                break
            else:
                wrong_game_inputs = 0
                continue
        else:
            wrong_game_inputs += 1
            input_messages.wrong_game_input(wrong_game_inputs)
            if wrong_game_inputs == 4:
                print("GAME OVER")
                restart()
                break
            else:
                play_game = input("Simply type 'yes' if you want to play and 'no' if you don't: ").lower()


game()
