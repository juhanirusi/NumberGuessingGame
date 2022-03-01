from with_classes_test import CheckInput

is_user_input_valid = CheckInput()

guess = input("Make a guess: ")
if is_user_input_valid.check_user_input(guess):
    print("Input value: VALID")
else:
    print("Input value: NOT VALID")
