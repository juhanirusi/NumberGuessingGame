EASY_LEVEL_TURNS = 4
MEDIUM_LEVEL_TURNS = 3
HARD_LEVEL_TURNS = 2

def difficulty_level(user_input):

    difficulty = input(user_input).lower()

    if difficulty == 'easy':
        return EASY_LEVEL_TURNS
    elif difficulty == 'medium':
        return MEDIUM_LEVEL_TURNS
    elif difficulty == 'hard':
        return HARD_LEVEL_TURNS
    else:
        print("Your input isn't quite what I was expecting, so I'll set the difficulty to 'easy'.")
        return EASY_LEVEL_TURNS