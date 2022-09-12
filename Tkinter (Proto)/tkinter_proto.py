import random
from tkinter import *
from tkinter import ttk

# Python Logo Colors
LIGHT_BLUE = '#4B8BBE'
DARK_BLUE = '#306998'

LIGHT_YELLOW = '#FFE873'
DARK_YELLOW = '#FFD43B'

GRAY = '#646464'
WHITE = '#ffffff'


class StartGamePage(Frame):
    def __init__(self, *args, **kwargs):
        #Frame.__init__(self, *args, **kwargs)
        self.window = window

        self.label = Label(text="Do you want to play the game? 'yes' or 'no'?", bg=LIGHT_BLUE, fg=WHITE, font=("Courier", 24)).place(relx=0.5, rely=0.1, anchor=CENTER)

        self.user_input = Entry(window, width=20, font=('Arial', 24))
        self.user_input.place(relx=0.5, rely=0.4, anchor=CENTER)

        self.button = Button(text="SUBMIT", command=self.play_game).place(relx=0.5, rely=0.6, anchor=CENTER)


    def play_game(self):
        user_input = self.user_input.get()
        if user_input in ('y', 'yup', 'yes', 'yeah'):
            self.answer = random.randint(1, 100)
            print("The correct answer is --> ", self.answer)  # TODO DELETE LATER!
            #self.guesses_left = set_difficulty.difficulty_level()
            print("Ok, the computer challenges you to guess a number between 1 and 100...")
            #self.guess_number()
        elif user_input in ('n', 'no', 'nope', 'no way'):
            print("Okay, I understand, see you next time.")
        else:
            print("Your input was confusing, I assume you don't want to play then.")


def center_window_on_screen(width=1100, height=650):
    screen_width = window.winfo_screenwidth() # Get screen width
    screen_height = window.winfo_screenheight() # Get screen height

    # calculate position x and y coordinates
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)

    # The first two parameters are the width and height of the window.
    # The last two parameters are x and y screen coordinates.
    window.geometry('%dx%d+%d+%d' % (width, height, x, y))


if __name__ == "__main__":
    window = Tk()
    window.title('Number Guessing Game')
    window.config(bg=LIGHT_BLUE)

    center_window_on_screen()

    StartGamePage(window)
    window.mainloop()
