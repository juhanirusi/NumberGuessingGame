from with_classes_test import CheckAnswer
import random

answer = random.randint(1, 100)

#play_game = str(input("Do you want to play a game? 'yes' or 'no': ")).lower()

user_guess = input("Enter your guess ")

check_answer = CheckAnswer(answer, user_guess)
check_answer.check_user_input(user_guess)