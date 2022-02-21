import random
import user_hints
import difficulty
import input_messages

def game(play_game):
    """
    This is the function for the main functionality of our game.
    """

    answer = random.randint(1, 100)

    # TODO DELETE AFTER FINISHED PROJECT!
    print("\nThe computer generated this number:", answer, "\n")

    # Just a set of numbers that have specific hints on them.
    # Check user_hints.py --> famous_number_hint() to get the idea!
    famous_numbers = {8, 99}

    # Assign multiple variables to the same value
    difficulty_not_set = user_plays_game = first_no_input = first_guess = True
    wrong_game_inputs = user_hint = guesses = 0

    def restart():
        """
        The function for restarting the program... if the user wants to.
        """

        global user_plays_game

        restart = input("Would you like to erase the computer's memory and restart the game? 'yes' or 'no': ")
        if restart in ('y', 'yup', 'yes'):
            game(play_game)
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
                    print(f"You still have {guesses_left} attempts remaining to guess the right number.")
                user_guess = input_messages.check_user_input("\nGuess again: ")

            guesses_left -= 1
            guesses += 1

            input_messages.wait_time(guesses, guesses_left)

            if guesses_left <= 0 and user_guess != answer:
                print("Oh no, your guess was wrong and you've ran out of guesses, so you lost the game. \U0001F61E")
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
                        if answer in famous_numbers:
                            user_hints.famous_number_hint(answer)
                    elif user_hint >= 3:
                        user_hints.user_hint_3(answer, user_guess)
                elif user_guess == answer:
                    print(f"CONGRATULATIONS! You guessed the number right, it was {answer}. The computer praises you! \U0001F64C")
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


if __name__ == "__main__":
    play_game = str(input("Do you want to play a game? 'yes' or 'no': ")).lower()
    game(play_game)
