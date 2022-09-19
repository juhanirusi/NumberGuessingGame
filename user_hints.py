class UserHints:
    """
    Used to display hints for the user based on the amount of
    guesses they've made and the type of number the correct answer is.
    """
    def __init__(self):
        """
        Used to hold the numbers the first hint uses to
        tell the user the range in which the correct answer is
        """
        self.number_ranges = [
            (1, 10),
            (11, 20),
            (21, 30),
            (31, 40),
            (41, 50),
            (51, 60),
            (61, 70),
            (71, 80),
            (81, 90),
            (91, 100)
        ]

    def user_hint_1(self, answer, guess):
        """
        The first user hint that tells the user the range of
        numbers that includes the correct answer and sending a
        message depending if the user input is out of the correct
        answer range or outside of it.
        """
        for num_range in self.number_ranges:
            if answer in range(num_range[0], (num_range[1] + 1)):
                from_number = num_range[0]
                to_number = num_range[1]

        if guess in range(from_number, to_number):
            print(f"Not quite. But you're right, the number is between {from_number} and {to_number}.")
        else:
            print(f"Nope. Let me give you a hint, the number is between {from_number} and {to_number}.")

    def user_hint_2(self, answer, guess):
        """
        The second user hint tells the user whether or not
        the correct answer is an even number or not and shows
        a message to the user depending whether the user guessed
        an even or uneven number.
        """
        if answer % 2 == 0:
            if guess % 2 == 0:
                print("That's not the right number. But you're right, the number IS an even number.")
            else:
                print("Nope. Here's a tip, the number IS an even number.")
        else:
            if guess % 2 == 0:
                print("Nope. Here's a tip, the number ISN'T an even number.")
            else:
                print("That's not the right number. But you're right, the number ISN'T an even number.")

    def user_hint_3(self, answer, guess):
        """
        The third user hint takes the correct answer and the
        user guess and tells the user whether their guess is
        higher or lower than the correct answer.
        """
        if guess < answer:
            print("That's not the correct answer either. The correct answer is HIGHER than your guess.")
        else:
            print("That's not the correct answer either. The correct answer is LOWER than your guess.")

    def famous_number_hint(self, answer):
        """
        The 'famous_number_hint' is shown to the user
        when the answer is some of the answer set as famous.
        """
        print("\n\U0001F4A1EXTRA HINT!\U0001F4A1")
        match answer:
            case 99:
                print("This number is also the jersey number of the most successful ice hockey player\n")
            case 8:
                print("Turning this number sideways will resemble the infinity symbol\n")
            case _:
                pass  # This is done if answer is not found --> JUST IN CASE!
