import random
import user_hints
import input_messages
import set_difficulty

EASY_LEVEL_TURNS = 9
MEDIUM_LEVEL_TURNS = 6
HARD_LEVEL_TURNS = 3

# MOVE ALL THAT'S BELOW TO THE BEGINNING OF THE game() FUNCTION WHEN EVERYTHING IS DONE!
guesses = 1
answer = random.randint(1, 100)

print("\nThe computer generated this number:", answer, "\n")

# play_game = str(input("Do you want to play a game? 'yes' or 'no': ")).lower()
# MOVE ALL THAT'S ABOVE TO THE BEGINNING OF THE game() FUNCTION WHEN EVERYTHING IS DONE!


# FROM HERE--------------------------------------------------------------------
# wrong_input = True
# while wrong_input:
#     if play_game == "no":
#         wrong_input = False
#         play_game = str(input("Are you sure? The computer REALLY wants to play with you: ")).lower()
#         if play_game == "no":
#             print("""Oops, now you hurt the computer's feelings and it decided to leave to count zeros and ones.
#                     However, the computer left one last message to you, but apparently it got so mad that it didn't bother to translate it completely...\n
#                     "You are such a 01110000 01100001 01110010 01110100 01111001 00100000 01110000 01101111 01101111 01110000 01100101 01110010, and I don't never wanna play with you again!"
#                     ...I have no idea what that means, \U0001F914 but the computer isn't happy. \U0001F620 \n""")
#     elif play_game == "yes":
#         wrong_input = False
#         too_high_low_input = True
#         user_guess = int(input("Ok, the computer challenges you to guess a number between 1 and 100: "))
#         while too_high_low_input:
#             if user_guess > 100:
#                 user_guess = int(input("Well now you're going WAY over the roof. I can't take this to the computer when it explicitly said NUMBER BETWEEN 1 AND 100: "))
#             elif user_guess < 1:
#                 user_guess = int(input("Well now you're just messing with me. I can't take this to the computer when it explicitly said NUMBER BETWEEN 1 AND 100: "))
#             elif user_guess == float:
#                 user_guess = int(input("FLOAT: "))
#             else:
#                 too_high_low_input = False
#     elif play_game != 'no' or 'yes':
#         play_game = str(input("Sorry, I can't deliver that message to the computer \U0001F615 , so to (or not to) play the game, simply type 'yes' or 'no': ")).lower()

# if play_game == 'yes':
#     while user_guess != answer:
#         if guesses < 2:
#             user_hints.user_hint_1(answer, user_guess)
#         elif guesses < 3:
#             user_hints.user_hint_2(answer, user_guess)

#         user_guess = int(input("Guess again: "))
#         guesses += 1

#     else:
#         play_game = False
#         print(f"\nEXCELLENT! You guessed the number right, it was {answer}. The computer praises you! \U0001F64C")
#         if guesses == 1:
#             print(f"You got the number right with your first guess. THAT'S ASTONISHING, even the computer is amazed \U0001F632 \n")
#         else:
#             print(f"You got the number right with {guesses} guesses. GOOD JOB!\n")
#         print("The computer had one last message to you, but I wasn't able to translate it completely...")
#         print('"You are such a 01100110 01110101 01101110 person!" ...Whatever that means? \U0001F914\n')
# TO HERE--------------------------------------------------------------------
            
            


def game():

    play_game = str(input("Do you want to play a game? 'yes' or 'no': ")).lower()
    wrong_game_inputs = 0
    user_plays_game = True
    first_no_input = True
    user_guess_type = ""
    game_on = True
    

    def restart():
        """
        The function for restarting the program (if user wants to).
        """

        global user_plays_game

        restart = input("Would you like to restart the game, and erase the computer's memory? ")
        if restart == "yes":
            game()
        elif restart == "no":
            user_plays_game = False
            print("Ok, I'll quit the program. Goodbye.")
        else:
            user_plays_game = False
            print("Your input was confusing. Therefore I'll end the whole program.")
            

    while user_plays_game:
        if play_game == 'yes':
            user_guess = input("Ok, the computer challenges you to guess a number between 1 and 100: ")
            
            # FROM HERE...
            input_messages.check_user_input(user_guess)
            
            if type(input_messages.check_user_input(user_guess)) == int:
                user_guess = int(user_guess)
                while game_on:
                    input_messages.user_guessed_number(user_guess)
                    user_guess = int(input("Guess again: "))
            elif type(input_messages.check_user_input(user_guess)) == float:
                print("seems to work with float")
            elif type(input_messages.check_user_input(user_guess)) == str:
                print("seems to work with str")
            # ...TO HERE
        
        elif play_game == 'no':
            if first_no_input:
                play_game = str(input("Are you sure? The computer REALLY wants to play with you: ")).lower()
                first_no_input = False
            input_messages.does_user_want_to_play(play_game)
            if play_game == 'no':
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
