import random

# Let's assign guesses as 1 (because user has to guess at least once)
# Let's also generate a random integer between 1 and 100
guesses = 1
number = random.randint(1, 100)

# FOR TESTING PURPOSES, DELETE AFTER FINISHED PROJECT!
print("\nThe computer generated this number:", number, "\n")
# FOR TESTING PURPOSES, DELETE AFTER FINISHED PROJECT!

# Let's ask the user if they want to play a game
play_game = str(input("Do you want to play a game? 'yes' or 'no': ")).lower()

# Function for the first user hint
def user_hint_1():
    """
    This function checks the number range of the computer generated number
    from 'number_ranges' list and assigns it into the 'from_number' & 'to_number' variables.
    
    After that, based on user input, the function shows a proper message to help the user move forward in the game.
    """
    number_ranges = [(1,10), (11,20), (21,30), (31, 40), (41, 50), (51, 60), (61, 70), (71, 80), (81, 90), (91, 100)]
    
    for num_range in number_ranges:
        if number in range(num_range[0], num_range[1]):
            from_number = num_range[0]
            to_number = num_range[1]
            
    if user_guess in range(from_number, to_number):
        print(f"Not quite. But you're pretty close because the number is between {from_number} and {to_number}.")
    else:
        print(f"Nope. Let me give you the first hint, the number is between {from_number} and {to_number}.")

def user_hint_2():
    is_even_number = number % 2
    if is_even_number == 0:
        if user_guess % 2 == 0:
            print("That's not the right number. But you're right, the number IS an even number.")
        else:
            print("Nope. My next tip is that the number IS an even number.")
    else:
        if user_guess % 2 == 0:
            print("Nope. My next tip is that the number ISN'T an even number.")
        else:
            print("That's not the right number. But you're right, the number ISN'T an even number.")
    

wrong_input = True

while wrong_input:
    if play_game == "no":
        wrong_input = False
        play_game = str(input("Are you sure? The computer REALLY wants to play with you: ")).lower()
        if play_game == "no":
            print("""
                Oops, now you hurt the computer's feelings and it decided to leave to count zeros and ones.
                However, the computer left one last message to you, but apparently it got so mad that it didn't bother to translate it completely...\n
                "You are such a 01110000 01100001 01110010 01110100 01111001 00100000 01110000 01101111 01101111 01110000 01100101 01110010, and I don't never wanna play with you again!"
                ...I have no idea what that means, \U0001F914 but the computer isn't happy. \U0001F620 \n""")
    elif play_game == "yes":
        wrong_input = False
        too_high_low_input = True
        user_guess = int(input("Ok, the computer challenges you to guess a number between 1 and 100: "))
        while too_high_low_input:
            if user_guess > 100:
                user_guess = int(input("Well now you're going WAY over the roof. I can't take this to the computer when it explicitly said NUMBER BETWEEN 1 AND 100: "))
            elif user_guess < 1:
                user_guess = int(input("Well now you're just messing with me. I can't take this to the computer when it explicitly said NUMBER BETWEEN 1 AND 100: "))
            elif user_guess == float:
                user_guess = int(input("FLOAT: "))
            else:
                too_high_low_input = False

    else:
        play_game = str(input("Sorry, I can't deliver that message to the computer \U0001F615 , so to (or not to) play the game, simply type 'yes' or 'no': ")).lower()

if play_game == 'yes':
    while user_guess != number:
        if guesses < 2:
            user_hint_1()
        else:
            user_hint_2()
        
        user_guess = int(input("Guess again: "))
        guesses = guesses + 1
        
    else:
        play_game = False
        print(f"\nEXCELLENT! You guessed the number right, it was {number}. The computer praises you! \U0001F64C")
        if guesses == 1:
            print(f"You got the number right with your first guess. THAT'S ASTONISHING, even the computer is amazed \U0001F632 \n")
        else:
            print(f"You got the number right with {guesses} guesses. GOOD JOB!\n")
        print("The computer had one last message to you, but I wasn't able to translate it completely...")
        print('"You are such a 01100110 01110101 01101110 person!" ...Whatever that means? \U0001F914\n')
        
        
        
        
# TRY THIS WITH FLOAT, INT, STRING...

# def check_user_input(input):
#     try:
#         # Convert it into integer
#         val = int(input)
#         print("Input is an integer number. Number = ", val)
#     except ValueError:
#         try:
#             # Convert it into float
#             val = float(input)
#             print("Input is a float  number. Number = ", val)
#         except ValueError:
#             print("No.. input is not a number. It's a string")


# input1 = input("Enter your Age ")
# check_user_input(input1)

# input2 = input("Enter any number ")
# check_user_input(input2)

# input2 = input("Enter the last number ")
# check_user_input(input2)