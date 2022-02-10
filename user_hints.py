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
        print(f"\nNot quite. But you're right, the number is between {from_number} and {to_number}.")
    else:
        print(f"\nNope. Let me give you the first hint, the number is between {from_number} and {to_number}.")
        
# Function for the second user hint --> user_hints.user_hint_2(number, user_guess)
def user_hint_2(answer, user_guess):
    """
    Checks whether the random number is an even or uneven number,
    and is the user input an even or uneven number

    After that, based on user input, the function shows a proper message to help the user move forward in the game.
    """
    is_even_number = answer % 2
    if is_even_number == 0:
        if user_guess % 2 == 0:
            print("\nThat's not the right number. But you're right, the number IS an even number.")
        else:
            print("\nNope. My next tip is that the number IS an even number.")
    else:
        if user_guess % 2 == 0:
            print("\nNope. My next tip is that the number ISN'T an even number.")
        else:
            print("\nThat's not the right number. But you're right, the number ISN'T an even number.")

# HINT THAT TELLS THE USER WHAT ONE NUMBER (INT) THERE IS IN THE NUMBER IF ANSWER LARGER THAN 9
def user_hint_3(answer):
    print(f"\nOk, this is my last tip, the last number of the answer is {answer % 10}.")
    print("I bet that you're now able to figure it out. \U0001F609")