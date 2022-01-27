def wrong_play_game_input(wrong_play_game_inputs):
    """
    If the user inputs something else than 'yes' or 'no' to the play_game input these messages are shown
    """
    if wrong_play_game_inputs == 1:
        print("That's a wrong input, I can't forward this to the computer. perhaps you made a typo? \U0001F92D Try again...")
    elif wrong_play_game_inputs == 2:
        print("Well, now your playing games with me. \U0001F612 Try again...")
    elif wrong_play_game_inputs == 3:
        print("Ok now I'm getting annoyed, \U0001F624 mess with me again, and I'll end the game....")
    else:
        pass
