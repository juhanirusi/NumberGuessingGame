EASY_LEVEL_TURNS = 5
MEDIUM_LEVEL_TURNS = 4
HARD_LEVEL_TURNS = 3


class Set_Difficulty:
    def difficulty_level(self):

        difficulty = input(
            "Choose a difficulty. Type 'easy', 'medium' or 'hard': ").lower()

        if difficulty == 'easy':
            return EASY_LEVEL_TURNS
        elif difficulty == 'medium':
            return MEDIUM_LEVEL_TURNS
        elif difficulty == 'hard':
            return HARD_LEVEL_TURNS
        else:
            print(
                "Your input wasn't quite what I was expecting, so I'll set the difficulty to 'easy'.")
            return EASY_LEVEL_TURNS
