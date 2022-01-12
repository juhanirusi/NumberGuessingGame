import random

guesses = 1
number = random.randint(1, 50)

def user_hint_1():
    if user_guess == number:
        pass
    elif number in range(1, 11):
        print("A little hint, the number is between 1 and 10.")
    elif number in range(11, 21):
        print("A little hint, the number is between 11 and 20.")
    elif number in range(21, 31):
        print("A little hint, the number is between 21 and 30.")
    elif number in range(31, 41):
        print("A little hint, the number is between 31 and 40.")
    elif number in range(41, 51):
        print("A little hint, the number is between 41 and 50.")

# def count_guesses():
#     user_guess = int(input("Guess again: "))
#     # HOW TO GET VARIABLES INSIDE FUNCTIONS...
#     guesses = guesses + 1

play_game = str(input("Do you want to play a game? 'yes' or 'no': ")).lower()

wrong_input = True

while wrong_input:
    if play_game == "no":
        wrong_input = False
        play_game = str(input("Are you sure? The computer has waited all day to play with you: ")).lower()
        if play_game == "no":
            print("""\n
                Oops, now you hurt the computer's feelings and it decided to leave to count zeros and ones.
                However, the computer left one last message to you, but apparently it got so mad that it didn't bother to translate it completely...\n
                "You are such a 01110000 01100001 01110010 01110100 01111001 00100000 01110000 01101111 01101111 01110000 01100101 01110010, and I don't never wanna play with you again!"
                ...I have no idea what that means, but the computer isn't happy.\n""")
    elif play_game == "yes":
        wrong_input = False
        user_guess = int(input("Ok, the computer challenges you to guess a number between 1 and 50: "))
    else:
        play_game = str(input("Sorry, I can't deliver that message to the computer, so to (or not to) play the game, simply type 'yes' or 'no': ")).lower()

if play_game == 'yes':
    while user_guess != number:
        user_hint_1()
        user_guess = int(input("Guess again: "))
        guesses = guesses + 1
    else:
        play_game = False
        print(f"\nEXCELLENT! You guessed the number right, it was {number}. The computer praises you!")
        print(f"You got the number right with {guesses} guess(es). GOOD JOB!\n")
        print("The computer had one last message to you, but I wasn't able to translate completely...")
        print('"You are such a 01100110 01110101 01101110 person!" ...Whatever that means?\n')