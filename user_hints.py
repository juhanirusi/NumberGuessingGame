# Function for the second user hint --> user_hints.user_hint_1(number, user_guess)
def user_hint_1(answer, user_guess):
    """
    Checks the number range of the computer generated number
    from 'number_ranges' list and assigns it into the 'from_number' & 'to_number' variables.

    After that, based on user input, the function shows a proper message to help the user move forward in the game.
    """
    number_ranges = [(1, 10), (11, 20), (21, 30), (31, 40), (41, 50), (51, 60), (61, 70), (71, 80), (81, 90), (91, 100)]

    for num_range in number_ranges:
        if answer in range(num_range[0], (num_range[1] + 1)):
            from_number = num_range[0]
            to_number = num_range[1]

    if user_guess in range(from_number, to_number):
        print(f"Not quite. But you're right, the number is between {from_number} and {to_number}.")
    else:
        print(f"Nope. Let me give you a hint, the number is between {from_number} and {to_number}.")
        

# Function for the second user hint --> user_hints.user_hint_2(number, user_guess)
def user_hint_2(answer, user_guess):
    """
    Checks whether the random number is an even or uneven number,
    and is the user input an even or uneven number.

    After that, based on user input, the function shows a proper message to help the user move forward in the game.
    """
    
    if answer % 2 == 0:
        if user_guess % 2 == 0:
            print("That's not the right number. But you're right, the number IS an even number.")
        else:
            print("Nope. My next tip is that the number IS an even number.")
    else:
        if user_guess % 2 == 0:
            print("Nope. My next tip is that the number ISN'T an even number.")
        else:
            print("That's not the right number. But you're right, the number ISN'T an even number.")


# HINT THAT TELLS THE USER IF THE THEIR GUESS IS HIGHER OR LOWER THAN THE CORRECT ANSWER
def user_hint_3(answer, user_guess):
    if user_guess < answer:
        print("That's not the correct answer either. The correct answer is HIGHER than your guess.")
    else:
        print("That's not the correct answer either. The correct answer is LOWER than your guess.")


# A HINT THAT TELLS THE USER IF THE NUMBER IS FAMOUS FROM SOMEWHERE
def famous_number_hint(answer):
    print("\n\U0001F4A1EXTRA HINT!\U0001F4A1")
    match answer:
        case 99:
            print("This number is also the jersey number of the most successful ice hockey player\n")
        case 8:
            print("Turning this number sideways will resemble the infinity symbol\n")
        case _:
            pass # This is done if answer is not found --> JUST IN CASE!
